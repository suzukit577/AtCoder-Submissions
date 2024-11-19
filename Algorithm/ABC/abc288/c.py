from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    graph[u].append(v)
    graph[v].append(u)
visited = [False for _ in range(n)]
n_connected = 0 # 連結成分の個数
for i in range(n):
    if not visited[i]:
        n_connected += 1
        queue = deque()
        queue.append(i)
        while len(queue) != 0:
            q = queue.popleft()
            for v in graph[q]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
print(m - n + n_connected)