N = int(input())
A = list(map(int, input().split()))
INF = 10**10
# dp[i][0]: 倒した回数が偶数回, dp[i][1]: 倒した回数が奇数回
dp = [[-INF] * 2 for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
    a = A[i - 1]
    # モンスターを倒さない場合
    dp[i][0] = max(dp[i - 1][0], dp[i][0])
    dp[i][1] = max(dp[i - 1][1], dp[i][1])
    # モンスターを倒す場合
    dp[i][1] = max(dp[i][1], dp[i - 1][0] + a)  # 倒すのが奇数回目になる場合
    dp[i][0] = max(dp[i][0], dp[i - 1][1] + 2 * a)  # 倒すのが偶数回目になる場合
print(max(dp[-1]))
