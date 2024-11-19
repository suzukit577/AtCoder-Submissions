def check_bingo(r, c, diag1, diag2, N):
    if r == N:
        return True
    if c == N:
        return True
    if diag1 == N or diag2 == N:
        return True
    return False


N, T = map(int, input().split())
A = list(map(int, input().split()))
row, col = [0] * N, [0] * N
diag1, diag2 = 0, 0

for i in range(T):
    r = (A[i] - 1) // N
    c = (A[i] - 1) % N
    row[r] += 1
    col[c] += 1
    if r == c:
        diag1 += 1
    if r + c == N - 1:
        diag2 += 1
    if check_bingo(row[r], col[c], diag1, diag2, N):
        print(i + 1)
        break
else:
    print(-1)

# 公式解説
N, T = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
row = [0] * N
col = [0] * N
diag = [0] * 2
for i in range(T):
    x = A[i] // N
    y = A[i] % N
    # 横
    row[x] += 1
    if row[x] == N:
        print(i + 1)
        exit()
    # 縦
    col[y] += 1
    if col[y] == N:
        print(i + 1)
        exit()
    # 左上 - 右下 方向の斜め
    if x == y:
        diag[0] += 1
        if diag[0] == N:
            print(i + 1)
            exit()
    # 右上 - 左下 方向の斜め
    if x + y == N - 1:
        diag[1] += 1
        if diag[1] == N:
            print(i + 1)
            exit()
print(-1)

# 公式解説 (別解)
N, T = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
inf = 1 << 30
mat = [[inf] * N for i in range(N)]
for i in range(T):
    x, y = A[i] // N, A[i] % N
    mat[x][y] = i + 1
ans = inf
# 横
for x in range(N):
    mx = 0
    for y in range(N):
        mx = max(mx, mat[x][y])
    ans = min(ans, mx)
# 縦
for y in range(N):
    mx = 0
    for x in range(N):
        mx = max(mx, mat[x][y])
    ans = min(ans, mx)
# 斜め
for x, y, dx, dy in [[0, 0, 1, 1], [0, N - 1, 1, -1]]:
    mx = 0
    for _ in range(N):
        mx = max(mx, mat[x][y])
        x += dx
        y += dy
    ans = min(ans, mx)
if ans == inf:
    ans = -1
print(ans)
