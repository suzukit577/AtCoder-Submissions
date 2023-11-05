n, k = map(int, input().split())
s = [input() for _ in range(n)]
ans = s[:k]
ans.sort()
for i in range(k):
    print(ans[i])