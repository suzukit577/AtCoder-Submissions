N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]
ans = 0
for i in range(N):
    cnt = sum(A[0][: i + 1] + A[1][i:])
    ans = max(ans, cnt)
print(ans)

# ユーザ解説 (DPで解く)
N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]
dp = [[0] * N for _ in range(2)]
dp[0][0] = A[0][0]
for i in range(2):
    for j in range(N):
        if j:
            dp[i][j] = max(dp[i][j], dp[i][j - 1] + A[i][j])
        if i:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + A[i][j])
print(dp[-1][-1])
