N, x = map(int, input().split())
A = list(map(int, input().split()))
ans = N
if sum(A) != x:
    A.sort()
    for i in range(N):
        if x < A[i]:
            ans = i
            break
        x -= A[i]
    else:
        ans = N - 1
print(ans)
