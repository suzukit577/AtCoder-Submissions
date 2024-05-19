X, Y, Z = map(int, input().split())
S = input()
N = len(S)
INF = 10 ** 9
dp = [[INF, INF] for _ in range(N + 1)] # dp[i][0]: i番目でOFF, dp[i][1]: i番目でON
dp[0][0] = 0
for i in range(N):
    if S[i] == 'a':
        dp[i + 1][0] = min(dp[i][0] + X, dp[i][1] + Z + X)
        dp[i + 1][1] = min(dp[i][0] + Z + Y, dp[i][1] + Y)
    if S[i] == 'A':
        dp[i + 1][0] = min(dp[i][0] + Y, dp[i][1] + Z + Y)
        dp[i + 1][1] = min(dp[i][0] + Z + X, dp[i][1] + X)
print(min(dp[-1]))