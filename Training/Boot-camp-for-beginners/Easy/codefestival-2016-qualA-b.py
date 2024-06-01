N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))
ans = 0
for i in range(N):
    if A[A[i]] == i:
        ans += 1
print(ans // 2)
