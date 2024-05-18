N, K = map(int, input().split())
r = N % K
ans = min(r, K - r)
print(ans)