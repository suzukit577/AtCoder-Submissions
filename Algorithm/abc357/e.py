from collections import deque


def topological_sort(G, into_num):
    """
    参考: https://output-zakki.com/topological_sort/
    """
    # 入ってくる有向辺を持たないノードを列挙
    q = deque()
    # V: 頂点数
    for i in range(len(G)):
        if into_num[i] == 0:
            q.append(i)

    # 以下、幅優先探索
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for adj in G[v]:
            into_num[adj] -= 1  # 入次数を減らす
            if into_num[adj] == 0:
                q.append(adj)  # 入次数が0になったら、キューに入れる

    return ans


N = int(input())
A = list(map(int, input().split()))
into_num = [0] * N
for i in range(N):
    into_num[A[i] - 1] += 1
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i].append(A[i] - 1)
top_sorted_graph = topological_sort(graph, into_num)

# 各頂点から到達可能な頂点数の合計を求めたい
ans = [0] * N
for u in top_sorted_graph[::-1]:
    for v in graph[u]:
        ans[u] += 1 + ans[v]
print(sum(ans))
