S = input()
N = len(S)
last, now, ans = "", "", 0
for s in S:
    now += s
    if now == last:
        continue
    last, now = now, ""
    ans += 1
print(ans)

# 公式解説
S = input()
N = len(S)
dp = [0] * (N + 1)  # N (= 1,2,...) 文字目までの最大分割数
dp[1] = dp[2] = 1
if S[0] != S[1]:
    dp[2] += 1
for i in range(3, N + 1):
    if S[i - 1] != S[i - 2]:
        # 連続する文字が異なるなら1文字ずつ分ける
        dp[i] = dp[i - 1] + 1
    else:
        # 連続する文字が同じなら S[i - 3], S[i - 2],
        # S[i - 1] の 3文字を 1文字, 2文字 と分ける
        dp[i] = dp[i - 3] + 2
print(dp[-1])
