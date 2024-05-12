N = int(input())
A = sorted(list(map(int, input().split())))
MOD = 10 ** 8
ans = 0

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