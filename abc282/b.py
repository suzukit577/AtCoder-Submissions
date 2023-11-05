n, m = map(int, input().split())
s = [input() for i in range(n)]
cnt = 0

for i in range(n-1):
    for j in range(i+1, n):
        can = True
        for k in range(m):
            if s[i][k] == 'x' and s[j][k] == 'x':
                can = False
        if can:
            cnt += 1

print(cnt)