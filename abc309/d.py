# 公式解説
from collections import deque

def get(G, s):
    # G: グラフの隣接行列, s: 頂点
    n = len(G) # n: グラフの頂点数
    dist = [-1] * n # dist[i]: 頂点 s から頂点 i までの最短距離
    dist[s] = 0
    Q = deque()
    Q.append(s)
    while len(Q) > 0:
        x = Q.popleft()
        for y in G[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                Q.append(y)
    return max(dist)

N1, N2, M = map(int, input().split())
G = [[] for _ in range(N1 + N2)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)
print(get(G, 0) + get(G, N1 + N2 - 1) + 1)