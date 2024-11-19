# evima 解説
from bisect import bisect_left, bisect_right

N, Q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for _ in range(Q):
    b, k = map(int, input().split())
    lo, hi = -1, 10**9  # 距離（探索範囲）の下限と上限
    while lo + 1 < hi:
        mi = (lo + hi) // 2
        c = bisect_right(a, b + mi) - bisect_left(a, b - mi)
        if c >= k:
            hi = mi
        else:
            lo = mi
    print(hi)
