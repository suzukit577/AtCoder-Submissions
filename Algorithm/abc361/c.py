N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = 10**9
for i in range(K + 1):
    diff = A[i + N - K - 1] - A[i]
    if diff < ans:
        ans = diff
print(ans)

# evima 解説
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = 10**9
for i in range(K + 1):
    ans = min(ans, A[i + N - K - 1] - A[i])
print(ans)
