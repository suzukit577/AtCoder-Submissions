N = int(input())
D, X = map(int, input().split())
ans = 0
for _ in range(N):
    A = int(input())
    day = 1
    while day <= D:
        ans += 1
        day += A
print(ans + X)
