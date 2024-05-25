A, B = map(int, input().split())
ans = 0
for i in range(A, B + 1):
    if str(i) == str(i)[::-1]:
        ans += 1
print(ans)

# 公式解説 (数字が5桁であることを利用する)
A, B = map(int, input().split())
ans = 0
for i in range(A, B + 1):
    s, t = i % 10, i // 10000 % 10
    u, v = i // 10 % 10, i // 1000 % 10
    if s == t and u == v:
        ans += 1
print(ans)
