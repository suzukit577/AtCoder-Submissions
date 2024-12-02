# 公式解説 - 非再帰
N, M = map(int, input().split())
W = [[]]
for i in range(1, N + 1):
    V = []
    for a in W:
        start = 1 if i == 1 else a[-1] + 10
        for x in range(start, M - 10 * (N - i) + 1):
            na = a + [x]
            V.append(na)
    W = V
X = len(W)
print(X)
for w in W:
    print(*w)


# 公式解説 - 再帰
import sys

sys.setrecursionlimit(10**6)


def dfs(v: list[int], ans: list[list[int]]) -> list[list[int]]:
    length = len(v)
    if length == N:
        ans.append(v)
        return
    start = 1 if length == 0 else v[-1] + 10
    for i in range(start, M - 10 * (N - length - 1) + 1):
        nxt = v + [i]
        dfs(nxt, ans)
    return ans


N, M = map(int, input().split())
ans = []
ans = dfs([], ans)
X = len(ans)
print(X)
for a in ans:
    print(*a)


# ユーザ解説 - Pythonで楽な解法 by hiro1729
from itertools import combinations

N, M = map(int, input().split())
ans = []
# itertools.combinations(p, r): リスト p の長さ r の部分列をソートして重複なしで返す関数
for c in combinations(list(range(1, M - 9 * (N - 1) + 1)), N):
    l = list(c)
    for i in range(1, N):
        l[i] += 9 * i
    ans.append(l)
X = len(ans)
print(X)
for a in ans:
    print(*a)
