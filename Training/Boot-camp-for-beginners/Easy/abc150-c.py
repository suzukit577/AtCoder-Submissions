import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
perm = list(itertools.permutations([i for i in range(1, N + 1)]))
print(abs(perm.index(P) - perm.index(Q)))
