# bit 全探索
n, m = map(int, input().split())
a = []
for i in range(m):
    c = int(input())
    a.append(list(map(int, input().split())))
ans = 0
for b in range(1 << m): # for b in range(2 **m): と等価
    s = set()
    for i in range(m):
        if (b >> i) & 1: # b の i-bit 目を見る
            for x in a[i]:
                s.add(x)
    if len(s) == n:
        ans += 1
print(ans)