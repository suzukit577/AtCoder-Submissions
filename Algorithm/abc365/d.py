N = int(input())
S = input()
# dp[i][j]: i 回目に j (0: Rock, 1: Paper, 2: Scissors) を出した時の最大勝利数
dp = [[0] * 3 for _ in range(N + 1)]
hand_index = {"R": 0, "P": 1, "S": 2}
win_against = {"R": 2, "P": 0, "S": 1}
for i in range(1, N + 1):
    # 青木くんの手に対応するインデックス
    current_hand = hand_index[S[i - 1]]
    for j in range(3):
        if j != current_hand:  # 連続する手が異なる必要がある
            dp[i][j] = max(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])
            if j == win_against[S[i - 1]]:
                dp[i][j] += 1
print(max(dp[-1]))
