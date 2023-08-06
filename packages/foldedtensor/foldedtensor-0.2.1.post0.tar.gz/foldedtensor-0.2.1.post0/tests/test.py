import random
import timeit

import torch
#import nestedtensor
from foldedtensor import as_folded_tensor

def perf(fn, n=1000, repeat=10):
    totals = timeit.repeat(fn, number=n, repeat=repeat)
    return (min(totals) / n) * 1000


rand_nested_list = [
    [random.randint(0, 5) for _ in range(random.randint(1, 50))] for _ in range(200)
] + [[random.randint(0, 10) for _ in range(1000)]]

ft = as_folded_tensor(
    rand_nested_list,
    data_dims=("words",),
    full_names=("samples", "words"),
    dtype=torch.long,
).to(torch.device("mps"))

lengths = [
    torch.as_tensor(length)
    for length in ft.lengths
]


#
#ft = as_folded_tensor(
#    [
#        [[1], [], [], [], [2, 3]],
#        [[4, 3]],
#    ],
#    data_dims=("words",),
#    full_names=("samples", "lines", "words"),
#)
#
#print(ft.shape)
#print(ft.refold("samples", "lines", "words"))
#exit()


def sum_all_words_per_sample():
    ids = torch.arange(lengths[0][0])
    for i in range(1, len(lengths)):

        ids = torch.repeat_interleave(
            ids, lengths[i],
            output_size=len(lengths[i+1]) if i < len(lengths) -1 else ft.size(len(ft.data_dims) - 1))

    out = torch.zeros(ft.lengths[0][0], ft_embedding.shape[-1], device=torch.device("cpu"))
    out.index_add_(source=ft_embedding.as_tensor().to('cpu'), dim=0, index=ids.to('cpu'))

    return out

#print("GET IDS", perf(get_indices), "ms")


embedder = torch.ones(128).to(torch.device("mps"))
ft_embedding = ft.refold("words").unsqueeze(-1) * embedder
refolded = ft_embedding.refold("samples", "words")

# nt = nestedtensor.nested_tensor([torch.tensor(sub) for sub in rand_nested_list])
#nt_embedding = nt.unsqueeze(-1) * embedder

print("------")
#print((nt_embedding.sum(1, keepdim=True).to_padded_tensor(0).squeeze(1) - ft_embedding.refold("samples", "words").sum(1)).mean(0))
#print((sum_all_words_per_sample() - ft_embedding.refold("samples", "words").sum(1)).mean(0))
print("------")

#print("FT NEW REFOLD", perf(lambda: ft_embedding.refold_2("samples", "words").sum(1, keepdim=True)), "ms")
print("FT OLD REFOLD", perf(lambda: ft_embedding.refold("samples", "words").sum(1, keepdim=True)), "ms")
print("FT INDEX ADD", perf(sum_all_words_per_sample), "ms")
print("FT ONLY SUM", perf(lambda: refolded.sum(1, keepdim=True)), "ms")

# print(nt_embedding.nested_size())
# print(nt_embedding.size(0), "-", nt_embedding.size(2))

# print("NT SUM BASE", perf(lambda: nt_embedding.sum(1, keepdim=True).to_padded_tensor(0)), "ms")
# print("NT SUM PAD", perf(lambda: nt_embedding.to_padded_tensor(0).sum(1, keepdim=True)), "ms")

exit(0)

