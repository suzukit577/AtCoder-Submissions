K = int(input())
C = list(map(int, input().split()))
MOD = 998244353

# dp[i][j]: i番目までの文字で長さがjの文字列を作る方法の数
dp = [[0] * (K + 1) for _ in range(27)]
dp[0][0] = 1  # 空文字列は1通り存在する

# 各文字についてDPを計算
for i in range(1, 27):
    for j in range(K + 1):
        dp[i][j] = dp[i - 1][j]  # 文字iを使わない場合

        # 文字iを1回からC[i-1]回まで使う
        for k in range(1, C[i - 1] + 1):
            if j - k >= 0:
                dp[i][j] += dp[i][j - k]
                dp[i][j] %= MOD

# 答えはdp[1]からdp[26]までの長さが1以上K以下の文字列の総和
result = sum(dp[i][j] for i in range(1, 27) for j in range(1, K + 1)) % MOD

print(result)
