H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
row_counts = [row.count('#') for row in S]
column_counts = [sum(S[i][j] == '#' for i in range(H)) for j in range(W)]
row_counts = [float('inf') if x == 0 else x for x in row_counts]
column_counts = [float('inf') if x == 0 else x for x in column_counts]
ans_row = row_counts.index(min(row_counts)) + 1
ans_col = column_counts.index(min(column_counts)) + 1
print(ans_row, ans_col)

# 公式解説
"""
U := (クッキーが置かれている行の番号の最小値)
D := (クッキーが置かれている行の番号の最大値)
L := (クッキーが置かれている列の番号の最小値)
R := (クッキーが置かれている列の番号の最大値)
として，以下の方針のアルゴリズムで求解可能．
1) U, D, L, R を求める．これは全てのマスについて全探索すれば計算できる．
2) (U, L) を左上，(D, R) を右下とする部分長方形の範囲で '.' になっているマスが答えである．
時間計算量は O(HW) で，ACするのに十分高速．
"""
H, W = map(int, input().split())
S = [input() for _ in range(H)]
U, D, L, R = float('inf'), -float('inf'), float('inf'), -float('inf')
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            U = min(U, i); D = max(D, i)
            L = min(L, j); R = max(R, j)
for i in range(U, D + 1):
    for j in range(L, R + 1):
        if S[i][j] == '.':
            print(i + 1, j + 1)

# ユーザー解説
"""
'.' のマスであって，上下左右にある '#' の数が2以上であるような場所が答え．計算量は O(HW)．
"""
def countAdjacentSharp(H, W, S, i, j):
    cnt = 0
    if i - 1 >= 0 and S[i - 1][j] == '#':
        cnt += 1
    if i + 1 <= H - 1 and S[i + 1][j] == '#':
        cnt += 1
    if j - 1 >= 0 and S[i][j - 1] == '#':
        cnt += 1
    if j + 1 <= W - 1 and S[i][j + 1] == '#':
        cnt += 1
    return cnt

H, W = map(int, input().split())
S = [input() for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '.' and countAdjacentSharp(H, W, S, i, j) >= 2:
            print(i + 1, j + 1)