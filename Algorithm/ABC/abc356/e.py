# evima 解説
from collections import Counter

N = int(input())
A = sorted(map(int, input().split()))
M = 10**6

a = [0] * (M + 1)  # 出現回数の累積和を格納するリスト
for x in A:
    a[x] += 1  # 出現回数を記録
for i in range(M):
    a[i + 1] += a[i]  # 累積和に更新

ans = 0
for v, t in Counter(A).items():  # O(M)
    ans += t * (t - 1) // 2
    for i in range(1, M // v + 1):  # O(log N)
        c = a[min(M, (i + 1) * v - 1)] - a[i * v - 1]
        if i == 1:
            c -= t
        ans += t * c * i
print(ans)

# 公式解説
cnt = [0] * (10**6 + 10)
N = int(input())
for c in map(int, input().split()):
    cnt[c] += 1
for i in range(len(cnt) - 1):
    cnt[i + 1] += cnt[i]
print(cnt[:9])
ans = 0
for c in range(1, 10**6 + 1):
    d = cnt[c] - cnt[c - 1]  # 配列 A に含まれる c の個数
    for kc in range(c, 10**6 + 1, c):  # c, 2 * c, 3 * c, ...
        k = kc // c  # A_j // A_i の個数
        ans += k * (cnt[min(10**6, kc + c - 1)] - cnt[kc - 1]) * d
    ans -= d * (d + 1) // 2
print(ans)
