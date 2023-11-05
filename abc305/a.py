N = int(input())
if N >= 98:
    print(100)
elif N % 5 <= 2:
    print(5 * (N // 5))
elif N % 5 >= 3:
    print(5 * (N // 5 + 1))

# 公式解説1
# 全体を5で割って考え，x = N / 5 に最も近い整数を求める
N = int(input())
print(round(N / 5) * 5)

# 次のようにも実装できる
# 「四捨五入」 = 「1 / 2 を足して切り捨て」
N = int(input())
print(((N + 2) // 5) * 5)

# 公式解説2
# 答えの候補である「0, 5, 10,...,100」の21個を全てチェックし，N との差が一番小さいものを出力する
N = int(input())
ans = 100
for i in range(0, 101, 5):
    if abs(N - ans) > abs(N - i):
        ans = i
print(ans)