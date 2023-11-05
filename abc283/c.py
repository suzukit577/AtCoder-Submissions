s = input()
n = len(s)
ans = 0
i = 0
while i < n:
    ans += 1
    if s[i] == '0' and i+1 < n and s[i+1] == '0':
        i += 2
    else:
        i += 1
print(ans)