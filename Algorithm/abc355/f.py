class UnionFind:
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == -1:
            return x  # x が根の場合は x を返す
        else:
            self.par[x] = self.root(self.par[x])  # 経路圧縮
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
            return False  # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]:  # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx  # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]:  # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry]  # rx 側の siz を調整する
        return True

    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]


def kruskal(N, edges):
    uf = UnionFind(N)
    edges.sort(key=lambda x: x[2])
    mst_cost = 0
    mst_edges = []

    for u, v, w in edges:
        if not uf.issame(u, v):
            uf.unite(u, v)
            mst_cost += w
            mst_edges.append((u, v, w))

    return mst_cost, mst_edges


N, Q = map(int, input().split())
edges = []
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b, c))

queries = []
for _ in range(Q):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    queries.append((u, v, w))

mst_cost, mst_edges = kruskal(N, edges)
uf = UnionFind(N)
for u, v, w in mst_edges:
    uf.unite(u, v)

results = []
current_mst_cost = mst_cost

for u, v, w in queries:
    if not uf.issame(u, v):
        current_mst_cost += w
        uf.unite(u, v)
    results.append(current_mst_cost)

for result in results:
    print(result)
