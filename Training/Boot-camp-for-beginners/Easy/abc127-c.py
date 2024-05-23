N, M = map(int, input().split())
L, R = set(), set()
for _ in range(M):
    l, r = map(int, input().split())
    L.add(l)
    R.add(r)
print(max(min(R) - max(L) + 1, 0))

# 公式解説
N, M = map(int, input().split())
l, r = 1, N
for _ in range(M):
    L, R = map(int, input().split())
    if l < L:
        l = L
    if R < r:
        r = R
print(max(r - l + 1, 0))
