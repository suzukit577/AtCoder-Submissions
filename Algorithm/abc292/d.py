from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    graph[u].append(v)
    graph[v].append(u)
used = [False for _ in range(n)]
ans = True
for i in range(n):
    nv = 0; ne = 0
    if not used[i]:
        queue = deque()
        used[i] = True
        queue.append(i)
        nv += 1
        ne += len(graph[i])
        while len(queue) != 0:
            q = queue.popleft()
            for v in graph[q]:
                if not used[v]:
                    used[v] = True
                    queue.append(v)
                    nv += 1
                    ne += len(graph[v])
    ne //= 2
    if nv != ne:
        ans = False
print("Yes" if ans else "No")