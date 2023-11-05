from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
dd = defaultdict(int)
ans = []
for a in A:
    dd[a] += 1
    if dd[a] == 2:
        ans.append(a)
print(*ans)

# 公式解説
N = int(input())
A = list(map(int, input().split()))
cnt = [0] * (N + 1)
ans = []
for a in A:
    cnt[a] += 1
    if cnt[a] == 2:
        ans.append(a)
print(*ans)