# evima 解説
from collections import defaultdict

N, K = map(int, input().split())
S = input()
MOD = 998244353

dp = [defaultdict(int) for _ in range(N + 1)]
dp[0][""] = 1


# 長さ K の文字列の回文判定
def p(s):
    return len(s) == K and s == s[::-1]


for i in range(N):
    for k, v in dp[i].items():
        for c in "AB":
            if S[i] in [c, "?"] and not p(k + c):
                nk = (k + c)[-(K - 1) :]
                dp[i + 1][nk] = (dp[i + 1][nk] + v) % MOD

print(sum(dp[N].values()) % MOD)
