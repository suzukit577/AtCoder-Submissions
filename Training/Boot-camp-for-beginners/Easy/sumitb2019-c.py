X = int(input())
dp = [False] * (10**6 + 1)
dp[0] = True
for x in range(X):
    if dp[x]:
        for d in range(6):
            dp[x + d + 100] = True
print("1" if dp[X] else "0")
