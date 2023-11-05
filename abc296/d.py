n, m = map(int, input().split())
ans = 2 ** 18
for i in range(1, n):
    x = (m+i-1) // i
    if x <= n:
        ans = min(ans, i*x)
    if i > x:
        break
if ans == 2 ** 18:
    print(-1)
else:
    print(ans)