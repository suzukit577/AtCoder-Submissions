N = int(input())
B = list(map(int, input().split()))
A = [0] * N
for i in range(N - 1):
    A[i], A[i + 1] = B[i], B[i]
    if i > 0 and A[i] > B[i - 1]:
        A[i] = B[i - 1]
print(sum(A))

# 公式解説
N = int(input())
B = [10**6] + list(map(int, input().split())) + [10**6]
A = [0] * (N + 1)
for i in range(1, N + 1):
    A[i] = min(B[i - 1], B[i])
print(sum(A))

# ユーザ解説
N = int(input())
B = list(map(int, input().split()))
ans = 0
ans += B[0]
for i in range(1, N - 1):
    ans += min(B[i - 1], B[i])
ans += B[N - 2]
print(ans)
