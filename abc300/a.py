n, a, b = map(int, input().split())
c = list(map(int, input().split()))
print(c.index(a + b) + 1)

# 公式解説
n, a, b = map(int, input().split())
c = list(map(int, input().split()))
ans = 0
for i in range(n):
    if a + b == c[i]:
        ans = i + 1
        break
print(ans)