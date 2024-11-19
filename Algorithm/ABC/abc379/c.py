# 公式解説
N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))
XA = sorted(zip(X, A))  # X の値でソート
sum_total, sum_idx = 0, 0
for x, a in XA:
    # もし現在の合計が x - 1 より小さい場合、目標に達しない
    if sum_total < x - 1:
        print(-1)
        break
    sum_total += a
    sum_idx += a * x
else:
    if sum_total != N:
        print(-1)
    else:
        # 合計からインデックスの重みを引いた値を出力
        print(N * (N + 1) // 2 - sum_idx)
