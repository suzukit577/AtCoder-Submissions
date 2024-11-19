# evima 解説
N, K = map(int, input().split())
MOD = 998244353

dp = [[0, 0] for _ in range(K + 1)]  # 一番左かどうか
dp[0][0] = 1
for i in range(K):
    p = 2 * (N - 1) * pow(N, -2, MOD) % MOD
    q = 2 * pow(N, -2, MOD)
    dp[i + 1][0] = (dp[i][0] * (1 - p) + dp[i][1] * q) % MOD
    dp[i + 1][1] = (dp[i][0] * p + dp[i][1] * (1 - q)) % MOD
print((1 * dp[K][0] + (2 + N) * pow(2, -1, MOD) * dp[K][1]) % MOD)
