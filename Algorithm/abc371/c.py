from itertools import permutations

N = int(input())
MG = int(input())
graph_G = [[0] * N for _ in range(N)]
graph_H = [[0] * N for _ in range(N)]
for _ in range(MG):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph_G[u][v] = 1
    graph_G[v][u] = 1
MH = int(input())
for _ in range(MH):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph_H[a][b] = 1
    graph_H[b][a] = 1
A = [[0] * N for _ in range(N - 1)]
for i in range(N - 1):
    A[i] = [0] * (i + 1) + list(map(int, input().split()))
min_cost = 10**12
for perm in permutations(range(N)):
    cost = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if graph_G[perm[i]][perm[j]] != graph_H[i][j]:
                cost += A[i][j]
    min_cost = min(min_cost, cost)
print(min_cost)
