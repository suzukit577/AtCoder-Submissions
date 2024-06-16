# evima 解説
K = int(input())
C = list(map(int, input().split()))
MOD = 998244353

fact = [1] * (K + 1)
for i in range(K):
    fact[i + 1] = fact[i] * (i + 1) % MOD
ifact = [1] * (K + 1)
ifact[K] = pow(fact[K], -1, MOD)
for i in range(K, 0, -1):
    ifact[i - 1] = ifact[i] * i % MOD


# 二校係数の計算
def c(n, r):
    return fact[n] * ifact[r] % MOD * ifact[n - r] % MOD


# DP の計算
dp = [[0] * (K + 1) for _ in range(len(C) + 1)]
dp[0][0] = 1
for i in range(len(C)):
    for j in range(K + 1):
        for k in range(min(C[i], K - j) + 1):
            dp[i + 1][j + k] += dp[i][j] * c(j + k, k) % MOD
            dp[i + 1][j + k] %= MOD
print(sum(dp[-1][1:]) % MOD)
