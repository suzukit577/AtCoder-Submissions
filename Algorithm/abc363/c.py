from itertools import permutations

N, K = map(int, input().split())
S = input()
perms = list(permutations(S))
print(perms)
