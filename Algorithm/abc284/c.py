# DFS(depth-first search)
def dfs(u, visited, to):
    visited[u] = True
    for v in to[u]:
        if visited[v]:
            continue # 既に訪れた頂点ならば何もしない
        dfs(v, visited, to) # 訪れていない頂点ならばもう一度 dfs を呼ぶ

N, M = map(int, input().split())
visited = [False for _ in range(N)] # 各頂点を訪れたかを記録するリスト
to = [[] for _ in range(N)] # 各頂点の行き先を記録するリスト
for i in range(M):
    u, v = map(int, input().split())
    u -= 1; v -= 1 # 頂点の番号を1減らしておく
    to[u].append(v); to[v].append(u) # 隣接リストに頂点を追加
ans = 0
for i in range(N):
    if not visited[i]:
        ans += 1
        dfs(i, visited, to)
print(ans)

# BFS(breadth-first search)
from collections import deque
N, M = map(int, input().split())
visited = [False for _ in range(N)] # 各頂点を訪れたかを記録するリスト
to = [[] for _ in range(N)] # 各頂点の行き先を記録するリスト
for i in range(M):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    to[u].append(v); to[v].append(u) # 隣接リストに頂点を追加
ans = 0
queue = deque()
for i in range(N):
    if visited[i]: # 頂点 i に訪れていれば何もしない
        continue
    ans += 1; visited[i] = True # 頂点 i に訪れていなければ， ans += 1 とし， i を訪れたと記録する
    queue.append(i) # 頂点 i をキューに追加
    while len(queue) != 0: # キューが空になるまで実行
        c = queue.popleft() # キューの左側から頂点 c を取り出す
        for d in to[c]: # 頂点 c の行き先であって，まだ訪れていない頂点を全て True にする
            if visited[d]:
                continue
            visited[d] = True
            queue.append(d)
print(ans)

# Union-Find
class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == -1:
            return x # x が根の場合は x を返す
        else:
            self.par[x] = self.root(self.par[x]) # 経路圧縮
            return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]: # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]: # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True

    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]

N, M = map(int, input().split())
uf = UnionFind(N)
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    uf.unite(u, v)
ans = 0
for i in range(N):
    if uf.root(i) == i: ans += 1
print(ans)