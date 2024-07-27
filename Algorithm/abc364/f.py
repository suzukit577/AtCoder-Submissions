# evima 解説
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


N, Q = map(int, input().split())
CLR = []
for i in range(Q):
    L, R, C = map(int, input().split())
    CLR.append((C, L - 1, R - 1))
uf = UnionFind(N)
r = [i for i in range(N)]
ans = 0
for C, L, R in sorted(CLR):
    p = L
    while p <= R:
        p = r[uf.root(p)]
        ans += C
        if p + 1 <= R:
            nr = r[uf.root(p + 1)]
            uf.unite(p, p + 1)
            r[uf.root(p)] = nr
        p += 1
print(ans if uf.size(0) == N else -1)
