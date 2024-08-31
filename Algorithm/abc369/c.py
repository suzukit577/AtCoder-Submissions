N = int(input())
A = list(map(int, input().split()))
ans, left, right = N, 0, 0
while left < N - 1:
    if right < N - 1 and (
        left == right or A[right + 1] - A[right] == A[left + 1] - A[left]
    ):
        right += 1
        ans += right - left
    else:
        left += 1
print(ans)

# 公式解説
N = int(input())
A = list(map(int, input().split()))

# evima 解説
N = int(input())
A = list(map(int, input().split()))
d = [A[i + 1] - A[i] for i in range(N - 1)]
combo, ans = 0, N
for i in range(N - 1):
    if i > 0 and d[i] == d[i - 1]:
        combo += 1
    else:
        combo = 1
    ans += combo
print(ans)
