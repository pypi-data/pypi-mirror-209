import torch
import torch.nn.functional as F
from torch import nn, einsum

from einops import rearrange, repeat

from colt5_attention import coor_descent
from colt5_attention.triton_coor_descent import triton_coor_descent

# helpers

def exists(val):
    return val is not None

def default(val, d):
    return val if exists(val) else d

# classes

class FeedForward(nn.Module):
    def __init__(
        self,
        dim,
        mult = 4,
        use_coor_descent = False,
        coor_descent_iters = 20,
        coor_descent_sparsity_k = None,
        coor_descent_eps = 1e-1,
        coor_descent_eps_init = 4.,
        coor_descent_eps_decay = 0.7,
    ):
        super().__init__()

        dim_hidden = int(dim * mult)

        self.use_coor_descent = use_coor_descent

        self.coor_descent_iters = coor_descent_iters
        self.coor_descent_sparsity_k = default(coor_descent_sparsity_k, dim_hidden // 10)
        self.coor_descent_eps = coor_descent_eps
        self.coor_descent_eps_init = coor_descent_eps_init
        self.coor_descent_eps_decay = coor_descent_eps_decay

        self.proj_in = nn.Sequential(
            nn.LayerNorm(dim),
            nn.Linear(dim, dim_hidden),
        )

        self.proj_out = nn.Linear(dim_hidden, dim)

    def forward(self, x):
        x = self.proj_in(x)

        if self.use_coor_descent:
            x = triton_coor_descent(
                x,
                n_iters = self.coor_descent_iters,
                k = self.coor_descent_sparsity_k,
                eps = self.coor_descent_eps,
                eps_init = self.coor_descent_eps_init,
                eps_decay = eslf.coor_descent_eps_decay,
                checkpoint_segments = self.coor_descent_iters // 5
            )
        else:
            x = F.gelu(x)

        return self.proj_out(x)

class Attention(nn.Module):
    def __init__(
        self,
        dim,
        dim_head = 64,
        heads = 8,
        use_coor_descent = False,
        coor_descent_iters = 20,
        coor_descent_sparsity_k = 1,
        coor_descent_eps = 1e-1,
        coor_descent_eps_init = 4.,
        coor_descent_eps_decay = 0.7,
        attn_null_kv = 0,
        learned_sparsity_k = False
    ):
        super().__init__()
        self.scale = dim_head ** -0.5
        self.heads = heads
        dim_inner = dim_head * heads

        self.use_coor_descent = use_coor_descent

        self.coor_descent_iters = coor_descent_iters
        self.coor_descent_sparsity_k = coor_descent_sparsity_k

        self.coor_descent_eps = coor_descent_eps
        self.coor_descent_eps_init = coor_descent_eps_init
        self.coor_descent_eps_decay = coor_descent_eps_decay

        self.to_learned_k = None
        if learned_sparsity_k:
            self.to_learned_k = nn.Linear(dim, heads)
            nn.init.constant_(self.to_learned_k.bias, -10)

        self.norm = nn.LayerNorm(dim)

        self.null_kv = nn.Parameter(torch.randn(2, heads, attn_null_kv, dim_head))

        self.to_qkv = nn.Linear(dim, dim_inner * 3, bias = False)
        self.to_out = nn.Linear(dim_inner, dim, bias = False)

    def forward(self, x):
        b, n, h, device, dtype = *x.shape[:2], self.heads, x.device, x.dtype
        x = self.norm(x)

        # get queries, keys, values, and split heads

        q, k, v = self.to_qkv(x).chunk(3, dim = -1)
        q, k, v = map(lambda t: rearrange(t, 'b n (h d) -> b h n d', h = h), (q, k, v))

        # add null key value if needed

        if self.null_kv.numel() > 0:
            nk, nv = map(lambda t: repeat(t, 'h n d -> b h n d', b = b), self.null_kv)
            k = torch.cat((nk, k), dim = -2)
            v = torch.cat((nv, v), dim = -2)

        # measure similarity

        q = q * self.scale
        sim = einsum('b h i d, b h j d -> b h i j', q, k)

        i, j = sim.shape[-2:]
        causal_mask = torch.ones((i, j), device = device, dtype = torch.bool).triu(j - i + 1)

        # whether to use coordinate descent or not

        if self.use_coor_descent:

            if exists(self.to_learned_k):
                sparsity_k = self.to_learned_k(x).sigmoid() * (self.coor_descent_sparsity_k - 1) + 1
                sparsity_k = rearrange(sparsity_k, 'b i h -> (b h i)')
            else:
                sparsity_k = torch.ones(i, device = device, dtype = dtype) * self.coor_descent_sparsity_k

            causal_mask = repeat(causal_mask, 'i j -> b h i j', b = sim.shape[0], h = sim.shape[1])

            attn = triton_coor_descent(
                sim,
                n_iters = self.coor_descent_iters,
                k = sparsity_k,
                eps = self.coor_descent_eps,
                eps_decay = self.coor_descent_eps_decay,
                eps_init = self.coor_descent_eps_init,
                mask = ~causal_mask,
                checkpoint_segments = self.coor_descent_iters // 5
            )

        else:
            sim = sim.masked_fill(causal_mask, -torch.finfo(sim.dtype).max)
            attn = sim.softmax(dim = -1)

        # aggregate

        out = einsum('b h i j, b h j d -> b h i d', attn, v)

        # combine heads

        out = rearrange(out, 'b h n d -> b n (h d)')
        return self.to_out(out)

# transformer

class Transformer(nn.Module):
    def __init__(
        self,
        *,
        num_tokens,
        dim,
        seq_len,
        depth,
        dim_head = 64,
        heads = 8,
        ff_mult = 4,
        attn_use_coor_descent = False,
        ff_use_coor_descent = False,
        attn_coor_descent_sparsity_k = 2,
        ff_coor_descent_sparsity_k = 2,
        coor_descent_iters = 15,
        coor_descent_eps = 1e-1,
        attn_null_kv = 0,
        learned_sparsity_k = False
    ):
        super().__init__()
        self.seq_len = seq_len

        self.token_emb = nn.Embedding(num_tokens, dim)
        self.pos_emb = nn.Embedding(seq_len, dim)

        self.layers = nn.ModuleList([])

        coor_kwargs = dict(
            coor_descent_iters = coor_descent_iters,
            coor_descent_eps = coor_descent_eps,
        )

        for _ in range(depth):
            self.layers.append(nn.ModuleList([
                Attention(
                    dim,
                    dim_head = dim_head,
                    heads = heads,
                    use_coor_descent = attn_use_coor_descent,
                    coor_descent_sparsity_k = attn_coor_descent_sparsity_k,
                    attn_null_kv = attn_null_kv,
                    learned_sparsity_k = learned_sparsity_k,
                    **coor_kwargs
                ),
                FeedForward(
                    dim,
                    ff_mult,
                    use_coor_descent = ff_use_coor_descent,
                    coor_descent_sparsity_k = ff_coor_descent_sparsity_k,
                    **coor_kwargs
                )
            ]))

        self.to_logits = nn.Sequential(
            nn.LayerNorm(dim),
            nn.Linear(dim, num_tokens)
        )

    def forward(self, x):
        n, device = x.shape[-1], x.device
        assert n <= self.seq_len

        x = self.token_emb(x)
        x = x + self.pos_emb(torch.arange(n, device = device))

        for attn, ff in self.layers:
            x = attn(x) + x
            x = ff(x) + x

        return self.to_logits(x)
