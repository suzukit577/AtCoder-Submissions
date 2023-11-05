s = input()
cnt = 0

for i in range(len(s)):
    if s[i] == 'v':
        cnt += 1
    else:
        cnt += 2

print(cnt)