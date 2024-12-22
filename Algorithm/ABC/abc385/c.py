N = int(input())
H = list(map(int, input().split()))
# dp[i][d] = i 番目のビルを起点として間隔 d で並ぶ高さが等しいビルの数
dp = [[0] * 3001 for _ in range(N)]
ans = 1
for i in range(N):
    for j in range(i + 1, N):
        d = j - i
        if H[i] == H[j]:
            dp[j][d] = dp[i][d] + 1
            ans = max(ans, dp[j][d] + 1)
print(ans)
