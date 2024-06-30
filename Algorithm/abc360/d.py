from bisect import bisect_left, bisect_right

N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))
left_dir, right_dir = [], []
for i in range(N):
    if S[i] == "0":
        left_dir.append(X[i])
    else:
        right_dir.append(X[i])
left_dir.sort()
right_dir.sort()
ans = 0
for rx in right_dir:
    pos_start = bisect_left(left_dir, rx)
    pos_end = bisect_right(left_dir, rx + 2 * (T + 0.1))
    ans += pos_end - pos_start
print(ans)

# evima 解説
from bisect import bisect_right

N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))

l = []
for i in range(N):
    if S[i] == "0":
        l.append(X[i])
l.sort()

ans = 0
for i in range(N):
    if S[i] == "1":
        ans += bisect_right(l, X[i] + 2 * T) - bisect_right(l, X[i])
print(ans)
