# evima 解説
N = int(input())
A = list(map(int, input().split()))

pos = [[] for _ in range(N + 1)]  # 各数値がどのインデックスに現れるか記録するリスト
for i, a in enumerate(A):
    pos[a].append(i + 1)

ans = 0
for i in range(N + 1):
    if pos[i]:
        # N 要素のリストにおける部分列の総数
        cnt = N * (N + 1) // 2
        p = [0] + pos[i] + [N + 1]
        for j in range(1, len(p)):
            # 区間 p[j - 1] + 1, ..., p[j] - 1
            # (数値 i が現れない区間) における部分列の総数
            cnt -= (p[j] - p[j - 1] - 1) * (p[j] - p[j - 1]) // 2
        ans += cnt
print(ans)
