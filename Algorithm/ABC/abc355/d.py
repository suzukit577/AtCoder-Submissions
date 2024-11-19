N = int(input())
events = []
for _ in range(N):
    l, r = map(int, input().split())
    events.append((l, "start"))
    events.append((r, "end"))
events.sort(
    key=lambda x: (x[0], x[1] == "end")
)  # 開始点と終了点が同じ場合は "start" を優先する
current_intervals = 0  # 現在重なっている区間の数
intersections = 0  # 区間の長複数
for event in events:
    if event[1] == "start":
        intersections += current_intervals
        current_intervals += 1
    else:
        current_intervals -= 1
print(intersections)

# 公式解説
# 余事象を考える
# -> 共通部分を持たない区間の組みの個数を求めて N * (N - 1) // 2 から引く
# 尺取り法で計算する
N = int(input())
l, r = [0] * N, [0] * N
for i in range(N):
    l[i], r[i] = map(int, input().split())
l.sort()
r.sort()
ans = N * (N - 1) // 2
j = 0
for i in range(N):
    while r[j] < l[i]:
        j += 1
    ans -= j
print(ans)

# ユーザ解説
from sortedcontainers import SortedList

N = int(input())
LR = sorted([tuple(map(int, input().split())) for _ in range(N)])
print(LR)
ans = 0
S = SortedList()
for l, r in LR[::-1]:
    ans += S.bisect_right(r)
    S.add(l)
print(ans)
