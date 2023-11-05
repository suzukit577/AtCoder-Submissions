from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
deg = [0] * n
for _ in range(m):
    a, b, c, d = input().split()
    a, c = int(a), int(c)
    a -= 1; c -= 1
    graph[a].append(c)
    graph[c].append(a)
    deg[a] += 1; deg[c] += 1
x, y = 0, 0
used = [False for _ in range(n)]
for i in range(n):
    if not used[i]:
        que = deque()
        used[i] = True
        que.append(i)
        flag = True
        while len(que) != 0:
            q = que.popleft()
            if deg[q] != 2:
                flag = False
            for v in graph[q]:
                if not used[v]:
                    que.append(v)
                    used[v] = True
        if flag:
            x += 1
        else:
            y += 1
print(x, y)