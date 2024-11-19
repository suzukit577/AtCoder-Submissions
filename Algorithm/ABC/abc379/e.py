# 公式解説
N = int(input())
S = input()
A = [(i + 1) * int(S[i]) for i in range(N)]
for i in range(1, N):
    A[i] += A[i - 1]
i, c = 0, 0
ans = []
while i < N or c > 0:
    if i < N:
        c += A[N - 1 - i]
    ans.append(c % 10)
    c //= 10
    i += 1
print(*ans[::-1], sep="")
