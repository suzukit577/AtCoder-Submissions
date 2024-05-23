N = int(input())
P = list(map(int, input().split()))
min_list = [0] * (N + 1)
min_list[0] = P[0]
for i in range(1, N):
    min_list[i] = min(min_list[i - 1], P[i - 1])
ans = 0
for i in range(N):
    if min_list[i] >= P[i]:
        ans += 1
print(ans)
