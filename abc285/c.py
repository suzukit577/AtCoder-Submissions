s = input()
n = len(s)
ans = 0
for i in range(n):
    ans += (ord(s[n-i-1]) - 64) * (26 ** i)
print(ans)