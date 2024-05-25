def check_bingo(row, col, diag1, diag2, N):
    for r in row:
        if r == N:
            return True
    for c in col:
        if c == N:
            return True
    if diag1 == N or diag2 == N:
        return True
    return False


N, T = map(int, input().split())
A = list(map(int, input().split()))

used = [[0] * N for _ in range(N)]
row = [0] * N
col = [0] * N
diag1 = 0
diag2 = 0

for i in range(T):
    y = (A[i] - 1) // N
    x = (A[i] - 1) % N
    if used[y][x] == 0:
        used[y][x] = 1
        row[y] += 1
        col[x] += 1
        if y == x:
            diag1 += 1
        if y == N - x - 1:
            diag2 += 1
        if check_bingo(row, col, diag1, diag2, N):
            print(i + 1)
            break
else:
    print(-1)
