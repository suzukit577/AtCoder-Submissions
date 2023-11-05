n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = []
re = []
for i in range(1,n+1):
    re.append(i)
    if i not in a:
        ans += sorted(re, reverse=True)
        re = []
print(*ans)