from collections import deque

def solve() -> bool:
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)] # 隣接リスト
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        graph[u].append(v); graph[v].append(u)
    if M != N - 1: # 条件1: 辺の数が N-1 本
        return False
    for i in range(N): # 条件2: 全ての頂点の次数が 2 以下
        if len(graph[i]) > 2:
            return False
    visited = [False for _ in range(N)] # 条件3: 連結性 -> BFS で判定
    queue = deque()
    visited[0] = True
    queue.append(0)
    while len(queue) != 0:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
    for i in range(N):
        if not visited[i]:
            return False
    return True

print("Yes" if solve() else "No")