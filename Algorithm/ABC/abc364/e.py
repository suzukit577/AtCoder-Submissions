# evima 解説
N, X, Y = map(int, input().split())
INF = 10**9

# dp[i][j][k]:
# 料理 1, 2, ..., i の中から j 個の料理を選ぶとき、
# 甘さの合計が k となるときのしょっぱさの合計の最小値
dp = [[[INF] * (X + 1) for j in range(i + 1)] for i in range(N + 1)]
dp[0][0][0] = 0
for i in range(N):
    A, B = map(int, input().split())
    for j in range(i + 1):
        for k in range(X + 1):
            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
            if k + A <= X:
                dp[i + 1][j + 1][k + A] = min(dp[i + 1][j + 1][k + A], dp[i][j][k] + B)

for j in range(N - 1, -1, -1):
    for k in range(X + 1):
        if dp[N][j][k] <= Y:
            print(j + 1)
            exit()
