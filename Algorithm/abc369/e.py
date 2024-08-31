# evima 解説
from itertools import permutations

N, M = map(int, input().split())
U, V, T = [0] * M, [0] * M, [0] * M
INF = 10**18
d = [[0 if i == j else INF for j in range(N)] for i in range(N)]
for i in range(M):
    U[i], V[i], T[i] = map(int, input().split())
    U[i], V[i] = U[i] - 1, V[i] - 1
    d[U[i]][V[i]] = d[V[i]][U[i]] = min(d[U[i]][V[i]], T[i])

# Floyd–Warshall Algorithm
for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

Q = int(input())
for _ in range(Q):
    K = int(input())
    B = list(map(lambda x: int(x) - 1, input().split()))
    ans = INF
    for p in permutations(B):
        for mask in range(1 << K):
            cost, cur = 0, 0
            for i in range(K):
                if mask >> i & 1:
                    cost += d[cur][U[p[i]]] + T[p[i]]
                    cur = V[p[i]]
                else:
                    cost += d[cur][V[p[i]]] + T[p[i]]
                    cur = U[p[i]]
            cost += d[cur][N - 1]
            ans = min(ans, cost)
    print(ans)
