# BFS
from collections import deque

N, D = map(int, input().split())
human = [tuple(map(int, input().split())) for _ in range(N)]
infected = [False] * N
infected[0] = True
queue = deque([0])
while len(queue) != 0:
    now = queue.popleft()
    for i in range(N):
        if not infected[i]:
            dist_sq = (human[i][0] - human[now][0]) ** 2 + (human[i][1] - human[now][1]) ** 2
            if dist_sq <= D ** 2:
                infected[i] = True
                queue.append(i)
for i in range(N):
    print('Yes' if infected[i] else 'No')

# DFS
N, D = map(int, input().split())
human = [tuple(map(int, input().split())) for _ in range(N)]
infected = [False] * N
infected[0] = True
stack = [0]
while len(stack) != 0:
    now = stack.pop()
    for i in range(N):
        if not infected[i]:
            dist_sq = (human[i][0] - human[now][0]) ** 2 + (human[i][1] - human[now][1]) ** 2
            if dist_sq <= D ** 2:
                infected[i] = True
                stack.append(i)
for i in range(N):
    print('Yes' if infected[i] else 'No')

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

def is_connected(i: int, j: int) -> bool:
    dist = (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2
    return dist <= D ** 2

N, D = map(int, input().split())
X = [0] * N; Y = [0] * N
for i in range(N): X[i], Y[i] = map(int, input().split())
uf = UnionFind(N)
for i in range(N):
    for j in range(N):
        if is_connected(i, j): uf.unite(i, j)
for i in range(N):
    print('Yes' if uf.issame(0, i) else 'No')