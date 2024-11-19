n, m = map(int, input().split())
a = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    a[u - 1].append(v)
    a[v - 1].append(u)

for (i, v) in enumerate(a):
    v.sort()
    print(len(v), *v)