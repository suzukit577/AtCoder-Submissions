MOD = 998244353
n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0,0] for _ in range(n)]
dp[0] = [1,1]
for i in range(1,n):
    # 配るDP
    for pre in range(2):
        for nxt in range(2):
            if data[i-1][pre] != data[i][nxt]:
                dp[i][nxt] += dp[i-1][pre]
    dp[i][0] %= MOD
    dp[i][1] %= MOD
print((dp[n-1][0] + dp[n-1][1]) % MOD)