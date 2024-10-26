S = [list(input()) for _ in range(8)]
ng_i, ng_j = set(), set()
for i in range(8):
    for j in range(8):
        if S[i][j] == "#":
            ng_i.add(i)
            ng_j.add(j)
ans = (8 - len(ng_i)) * (8 - len(ng_j))
print(ans)


# 公式解説-1 (マスごとに取られないか判定する)
# マス (i, j) にコマを置くことができるか判定する
def check_square(board: list[list[str]], i: int, j: int) -> bool:
    for b in board[i]:
        # すでに同じ行にコマが置かれていたら、コマを置くことはできない
        if b:
            return False
    for row in board:
        # すでに同じ列にコマが置かれていたら、コマを置くことはできない
        if row[j]:
            return False
    return True


board = [[c == "#" for c in input()] for _ in range(8)]
ans = 0
# それぞれのマスについて、
for i in range(8):
    for j in range(8):
        # コマが置けるなら答えを 1 増やす
        if check_square(board, i, j):
            ans += 1
print(ans)


# 公式解説-2 (コマごとに取れるマスを計算する)
board = [[c == "#" for c in input()] for _ in range(8)]
# 置くことができるマスを求める
# はじめすべて True で初期化
safe = [[True] * 8 for _ in range(8)]

for i, row in enumerate(board):
    for j, b in enumerate(row):
        # コマが置かれていたら
        if b:
            for k in range(8):
                # 同じ行のマスに置くことはできない
                safe[i][k] = False
                # 同じ列のマスに置くことはできない
                safe[k][j] = False
# 置くことができるマスの合計を出力
print(sum(+f for row in safe for f in row))


# ユーザ解説 (自分の提出コードと同じ解法)
row, column = [False] * 8, [False] * 8
board = [list(input()) for _ in range(8)]
for i in range(8):
    for j in range(8):
        if board[i][j] == "#":
            row[i] = True
            column[j] = True
print(row.count(False) * column.count(False))
