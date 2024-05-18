h, w = map(int, input().split())
s = [input() for i in range(h)]
t = [input() for i in range(h)]

ts = [[None for i in range(h)] for j in range(w)]
tt = [[None for i in range(h)] for j in range(w)]

for i in range(h):
    for j in range(w):
        ts[j][i] = s[i][j]
        tt[j][i] = t[i][j]

ts.sort()
tt.sort()

if ts == tt:
    print("Yes")
else:
    print("No")