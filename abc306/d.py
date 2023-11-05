N = int(input())
# dp[i][j]:
# 料理 i までの料理を食べるか下げてもらうか選択した時に，高橋くんの状態が j (0...高橋くんがお腹を壊していない，1...高橋くんがお腹を壊している) である時の，食べた料理の美味しさの総和の最大値
dp = [[-float('inf'), -float('inf')] for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    X, Y = map(int, input().split())
    dp[i + 1][0] = dp[i][0] # 食べない時
    dp[i + 1][1] = dp[i][1] # 食べない時
    if X == 0:
        dp[i + 1][0] = max(dp[i][0], dp[i][0] + Y, dp[i][1] + Y)
    else:
        dp[i + 1][1] = max(dp[i][1], dp[i][0] + Y)
print(max(dp[-1]))

# 公式解説
"""
動的計画法でこの問題を解くことを考えます．すると，どのような情報を保持するべきでしょうか？
結論から言うと，以下の DP テーブルを作成することでこの問題を解くことができます．
・dp[i][j]
    - 料理 i までの料理を食べるか下げてもらうか選択した時に，高橋くんの状態が j (0...高橋くんがお腹を壊していない，1...高橋くんがお腹を壊している) である時の，食べた料理の美味しさの総和の最大値
この問題が解けなかった方は，上で「どのような DP テーブルを作れば解けるか」を示したので，「DP テーブルの遷移はどうするべきか」を考えて実装してみてください．動的計画法の良い練習になります．
"""
N = int(input())
X = [0] * N; Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
dp = [[-float('inf'), -float('inf')] for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    if X[i] == 0:
        dp[i + 1][0] = max(dp[i][0], max(dp[i][0], dp[i][1]) + Y[i])
    else:
        dp[i + 1][1] = max(dp[i][1], dp[i][0] + Y[i])
    dp[i + 1][0] = max(dp[i + 1][0], dp[i][0])
    dp[i + 1][1] = max(dp[i + 1][1], dp[i][1])
print(max(dp[-1]))