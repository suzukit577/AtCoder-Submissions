# 公式解説 (尺取り法)
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = 10 ** 8
R = N
cnt, res = 0, 0
for i in range(N):
    R = max(R, i + 1)
    while R - 1 > i and A[R - 1] + A[i] >= M:
        R -= 1
    cnt += N - R
for i in range(N):
    res += A[i] * (N - 1)
res -= cnt * M
print(res)

# evima 解説
N = int(input())
A = list(map(int, input().split()))
M = 10 ** 8

cnt = [0] * (M + 1)
for a in A:
    cnt[a] += 1
for i in range(M):
    cnt[i + 1] += cnt[i]

p = 0
for a in A:
    p += N - cnt[M - a - 1]
    if 2 * a >= M:
        p -= 1
print((N - 1) * sum(A) - p // 2 * M)