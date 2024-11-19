# evima 解説
import pypyjit
import sys

pypyjit.set_param("max_unroll_recursion=-1")
sys.setrecursionlimit(10**9)

N = int(input())
g = [[] for _ in range(N)]
sum_c = 0
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    g[a - 1].append((b - 1, c))
    g[b - 1].append((a - 1, c))
    sum_c += c


def dfs(u, p):
    ret = (0, u)
    for v, c in g[u]:
        if v != p:
            d, x = dfs(v, u)
            ret = max(ret, (d + c, x))
    return ret


_, u = dfs(0, -1)
d, _ = dfs(u, -1)
print(2 * sum_c - d)
