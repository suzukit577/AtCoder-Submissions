import math
from itertools import permutations

N = int(input())
towns = []
for _ in range(N):
    x, y = map(int, input().split())
    towns.append((x, y))
dist = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j:
            dist[i][j] = math.sqrt(
                (towns[i][0] - towns[j][0]) ** 2 + (towns[i][1] - towns[j][1]) ** 2
            )
perms = list(permutations([i for i in range(N)]))
ans = 0
for p in perms:
    for i in range(N - 1):
        ans += dist[p[i]][p[i + 1]]
print(ans / len(perms))

# 別解
import math

N = int(input())
towns = []
for _ in range(N):
    x, y = map(int, input().split())
    towns.append((x, y))
dist = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j:
            dist[i][j] = math.sqrt(
                (towns[i][0] - towns[j][0]) ** 2 + (towns[i][1] - towns[j][1]) ** 2
            )
print(sum([sum(dist[i]) for i in range(N)]) / N)
