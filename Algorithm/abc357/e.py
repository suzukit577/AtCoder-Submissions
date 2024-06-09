# evima 解説 (ac-library-python の強連結成分分解)
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
