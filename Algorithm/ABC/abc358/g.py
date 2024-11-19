# evima 解説
H, W, K = map(int, input().split())
Si, Sj = map(lambda x: int(x) - 1, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

INF = 10**18
dp = [[[-INF] * W for _ in range(H)] for _ in range(H * W + 2)]
dp[0][Si][Sj] = 0
ans = 0
for t in range(min(K, H * W) + 1):
    for i in range(H):
        for j in range(W):
            ans = max(ans, dp[t][i][j] + (K - t) * A[i][j])
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W:
                    dp[t + 1][ni][nj] = max(dp[t + 1][ni][nj], dp[t][i][j] + A[ni][nj])
print(ans)
