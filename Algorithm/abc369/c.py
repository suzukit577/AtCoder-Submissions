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
