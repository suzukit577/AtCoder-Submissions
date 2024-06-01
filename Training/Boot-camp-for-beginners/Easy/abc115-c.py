N, K = map(int, input().split())
H = list()
for _ in range(N):
    H.append(int(input()))
H.sort()
ans = 10**10
for i in range(N - K + 1):
    ans = min(ans, H[i + K - 1] - H[i])
print(ans)
