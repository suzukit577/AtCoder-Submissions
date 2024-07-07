N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
left, right = 0, N - 1
ans = A[right] - A[left]
for i in range(K):
    pop_left, pop_right = A[right] - A[left + 1], A[right - 1] - A[left]
    if pop_left <= pop_right:
        ans = pop_left
        left += 1
    else:
        ans = pop_right
        right -= 1
print(ans)
