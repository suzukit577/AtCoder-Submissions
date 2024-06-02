# evima 解説
from collections import Counter

N = int(input())
A = sorted(map(int, input().split()))
M = 10**6

a = [0] * (M + 1)
for x in A:
    a[x] += 1
for i in range(M):
    a[i + 1] += a[i]

ans = 0
for v, t in Counter(A).items():
    ans += t * (t - 1) // 2
    for i in range(1, M // v + 1):
        c = a[min(M, (i + 1) * v - 1)] - a[i * v - 1]
        if i == 1:
            c -= t
        ans += t * c * i
print(ans)
