# 公式解説
H, W = map(int, input().split())
C = [input() for _ in range(H)]

def ok(i, j):
    return 0 <= i < H and 0 <= j < W

def test(i, j, d):
    for x in [+d, -d]:
        for y in [+d, -d]:
            s, t = i + x, j + y
            if not ok(s, t) or C[s][t] != '#':
                return False
    return True

N = min(H, W)
ans = [0 for _ in range(N + 1)]
for i in range(H):
    for j in range(W):
        if C[i][j] != '#':
            continue
        if test(i, j, 1):
            d = 1
            while test(i, j, d + 1):
                d += 1
            ans[d] += 1
print(' '.join(map(str, ans[1:])))

# 別解
H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]

def dfs(y, x):
    cnt = 1
    C[y][x] = '.'
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            y2, x2 = y + dy, x + dx
            if 0 <= y2 < H and 0 <= x2 < W and C[y2][x2] == '#':
                cnt += dfs(y2, x2)
    return cnt

ans = [0 for _ in range(min(H, W) + 1)]
for y in range(H):
    for x in range(W):
        if C[y][x] == '#':
            ans[dfs(y, x) // 4] += 1
print(' '.join(map(str, ans[1:])))