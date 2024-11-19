# 公式解説
from collections import deque

N, M = map(int, input().split())
graph = [list() for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a].append(b)
INF = 10**9
dist, queue = [INF] * N, deque()

dist[0] = 0
queue.append(0)

while len(queue) > 0:
    cur = queue.popleft()
    for u in graph[cur]:
        if u == 0:
            print(dist[cur] + 1)
            exit()
        if dist[u] == INF:
            dist[u] = dist[cur] + 1
            queue.append(u)

print(-1)
