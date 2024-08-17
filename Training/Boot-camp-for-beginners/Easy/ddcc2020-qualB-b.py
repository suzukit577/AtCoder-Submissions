N = int(input())
A = list(map(int, input().split()))
SA = [0] * (N + 1)
for i in range(N):
    SA[i + 1] = SA[i] + A[i]
ans = 10**16
for i in range(N + 1):
    ans = min(ans, abs(SA[i] - (SA[-1] - SA[i])))
print(ans)
