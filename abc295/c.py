from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
dd = defaultdict(int)
ans = 0
for ai in a:
    dd[ai] += 1
for k, v in dd.items():
    ans += v // 2
print(ans)