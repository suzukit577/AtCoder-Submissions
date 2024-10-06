N = int(input())
K = sorted(list(map(int, input().split())))
ans, diff = 0, 10**10
for mask in range(1 << N):
    A, B = 0, 0
    for i in range(N):
        if mask & (1 << i):
            A += K[i]
        else:
            B += K[i]
    diff_new = abs(A - B)
    if diff_new < diff:
        diff = diff_new
        ans = max(A, B)
print(ans)


# ユーザ解説 (別解: 再帰関数による実装)
import sys

sys.setrecursionlimit(10**6)


def dfs(pos: int) -> None:
    global A, B, ans
    if pos == N:
        ans = min(ans, max(A, B))  # N 個の部署について割り当てが終わったら答えを更新
        return
    # pos 番目の部署を A に割り当てた場合
    A += K[pos]
    dfs(pos + 1)
    A -= K[pos]
    # pos 番目の部署を B に割り当てた場合
    B += K[pos]
    dfs(pos + 1)
    B -= K[pos]
    return


N = int(input())
K = list(map(int, input().split()))
A, B, ans = 0, 0, 10**10
dfs(0)
print(ans)
