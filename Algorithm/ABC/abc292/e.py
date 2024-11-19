from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    graph[u].append(v)
ans = 0
for i in range(n):
    f = [False for _ in range(n)]
    f[i] = True
    queue = deque()
    queue.append(i)
    while len(queue) != 0:
        x = queue.popleft()
        for j in range(len(graph[x])):
            y = graph[x][j]
            if f[y]:
                continue
            f[y] = True
            queue.append(y)
            ans += 1
ans -= m
print(ans)