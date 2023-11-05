import copy

r, c = map(int, input().split())
b = [list(input()) for _ in range(r)]
ans = copy.deepcopy(b)
bomb = set([f"{i}" for i in range(10)])
for i in range(r):
    for j in range(c):
        if b[i][j] in bomb:
            bi = int(b[i][j])
            for k in range(bi+1):
                for l in range(bi-k+1):
                    if i-k >= 0 and j-l >= 0:
                        ans[i-k][j-l] = "."
                    if i-k >= 0 and j+l <= c-1:
                        ans[i-k][j+l] = "."
                    if i+k <= r-1 and j-l >= 0:
                        ans[i+k][j-l] = "."
                    if i+k <= r-1 and j+l <= c-1:
                        ans[i+k][j+l] = "."
for i in range(r):
    for j in range(c):
        print(ans[i][j], end="")
    print()

# 解説の実装
r, c = map(int, input().split())
b = [list(input()) for _ in range(r)]
blasted = [[False] * c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if not b[i][j].isdigit():
            continue
        power = int(b[i][j])
        for ni in range(r):
            for nj in range(c):
                if abs(i - ni) + abs(j - nj) <= power:
                    blasted[ni][nj] = True
for i in range(r):
    for j in range(c):
        if blasted[i][j]:
            b[i][j] = "."
for i in range(r):
    print("".join(b[i]))

# 原案者の実装
r, c = map(int, input().split())
b = [input() for _ in range(r)]
for i in range(r):
    for j in range(c):
        x = b[i][j]
        for i2 in range(r):
            for j2 in range(c):
                power = int(b[i2][j2]) if b[i2][j2].isdigit else -1
                if abs(i - i2) + abs(j - j2) <= power:
                    x = "."
        print(x, end="")
    print()