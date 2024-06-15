# evima 解説 (ac-library-python の強連結成分分解)
# オーバーキルではある
from atcoder.scc import SCCGraph

N = int(input())
a = list(map(lambda x: int(x) - 1, input().split()))
g = SCCGraph(N)
for i in range(N):
    g.add_edge(i, a[i])
r = [0] * N
for c in g.scc()[::-1]:
    if len(c) > 1 or a[c[0]] == c[0]:
        for u in c:
            r[u] = len(c)
    else:
        r[c[0]] = r[a[c[0]]] + 1
print(sum(r))

# 公式解説
"""
Functional Graph:
すべての頂点の出次数が 1 の有向グラフ

Functional Graph の性質:
G の連結成分が K 個あって C_1, C_2, ..., C_K とする．このとき，各連結成分には閉路が 1 つだけ存在する．

-> 連結成分ごとに独立に問題を解く
"""
