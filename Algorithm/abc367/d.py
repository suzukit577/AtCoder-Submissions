# evima 解説
N, M = map(int, input().split())
A = list(map(int, input().split()))
s = sum(A)
A += A

c = [0] * M  # 距離が M の 0, 1, ..., M - 1 倍のペアの個数
d, ans = 0, 0  # d: 累積和, ans: 条件を満たすペアの個数
for i in range(2 * N):
    if i >= N:
        c[(d - s) % M] -= 1
        ans += c[d % M]
    c[d % M] += 1
    d += A[i]
print(ans)
