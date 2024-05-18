N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))
ans = 0
price = dict()
for i in range(M):
    price[D[i]] = P[i + 1]
for c in C:
    if c in D:
        ans += price[c]
    else:
        ans += P[0]
print(ans)

# 公式解説
n, m = map(int, input().split())
c = list(input().split())
d = list(input().split())
p = list(map(int, input().split()))
ans = 0
for v in c:
    price = p[0]
    for j in range(m):
        if v == d[j]:
            price = p[j + 1]
            break
    ans += price
print(ans)