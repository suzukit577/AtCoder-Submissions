X, Y, Z = map(int, input().split())
S = input()
N = len(S)
dp = [[float('inf')] * 2 for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    if S[i] == 'a':
        dp[i + 1][0] = min(dp[i][0] + X, dp[i][1] + Z + X)
        dp[i + 1][1] = min(dp[i][0] + Z + Y, dp[i][1] + Y)
    else:
        dp[i + 1][0] = min(dp[i][0] + Y, dp[i][1] + Z + Y)
        dp[i + 1][1] = min(dp[i][0] + Z + X, dp[i][1] + X)

print(min(dp[-1][0], dp[-1][1]))


## 公式解説
X, Y, Z = map(int, input().split())
S = input()
N = len(S)
dp = [[float('inf')] * 2 for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    cur = 0 # S[i] が小文字か大文字かのフラグ
    if S[i] == 'a': pass
    else: cur = 1
    for j in range(2):
        for k in range(2):
            v = dp[i][j]
            if j != k: v += Z
            if cur == k: v += X
            else: v += Y
            dp[i + 1][k] = min(dp[i + 1][k], v)

print(min(dp[-1][0], dp[-1][1]))