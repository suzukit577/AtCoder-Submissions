from collections import deque
from collections import defaultdict

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
connected_num = defaultdict(int)
visited = [False for _ in range(N)]
for i in range(N):
    if not visited[i]:
        queue.append(i)
        visited[i] = True
        connected_num[i] += 1
    while len(queue) != 0:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                connected_num[i] += 1

ans = 0
for c in connected_num.values():
    ans += c * (c - 1) // 2
ans -= M
print(ans)

# 解説(evima)
import sys
import pypyjit

sys.setrecursionlimit(10**6)
pypyjit.set_param("max_unroll_recursion=-1")

N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
used = [False] * N

def dfs(u):
    used[u] = True
    res = 1
    for v in g[u]:
        if not used[v]:
            res += dfs(v)
    return res

ans = -M
for i in range(N):
    if not used[i]:
        s = dfs(i)
        ans += s * (s - 1) // 2
print(ans)