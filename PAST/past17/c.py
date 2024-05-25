N = int(input())
A = list(map(int, input().split()))
P = list(map(int, input().split()))
ans = 0
for i in range(N):
    ans += P[A[i] - 1]
print(ans)
