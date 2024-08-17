N = int(input())
A = sorted(list(map(int, input().split())))
ans = 0
for i in range(N, 3 * N, 2):
    ans += A[i]
print(ans)
