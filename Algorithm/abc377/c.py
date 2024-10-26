# version-1
def is_in_board(i: int, j: int) -> bool:
    return 0 <= i <= N - 1 and 0 <= j <= N - 1


def target_grid(a: int, b: int, target: set[int]) -> set[int]:
    target.add((a, b))
    if is_in_board(a + 2, b + 1):
        target.add((a + 2, b + 1))
    if is_in_board(a + 1, b + 2):
        target.add((a + 1, b + 2))
    if is_in_board(a - 1, b + 2):
        target.add((a - 1, b + 2))
    if is_in_board(a - 2, b + 1):
        target.add((a - 2, b + 1))
    if is_in_board(a - 2, b - 1):
        target.add((a - 2, b - 1))
    if is_in_board(a - 1, b - 2):
        target.add((a - 1, b - 2))
    if is_in_board(a + 1, b - 2):
        target.add((a + 1, b - 2))
    if is_in_board(a + 2, b - 1):
        target.add((a + 2, b - 1))
    return target


N, M = map(int, input().split())
target = set()
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    target = target_grid(a, b, target)
print(N**2 - len(target))


# version-2
def is_in_board(i: int, j: int) -> bool:
    return 0 <= i <= N - 1 and 0 <= j <= N - 1


def target_grid(a: int, b: int, target: set[tuple[int, int]]) -> set[tuple[int, int]]:
    directions = [
        (2, 1),
        (1, 2),
        (-1, 2),
        (-2, 1),
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1),
    ]
    target.add((a, b))
    for di, dj in directions:
        ni, nj = a + di, b + dj
        if is_in_board(ni, nj):
            target.add((ni, nj))
    return target


N, M = map(int, input().split())
target = set()
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    target = target_grid(a, b, target)
print(N**2 - len(target))


# 公式解説
N, M = map(int, input().split())
bad_cell = set()  # 置くことができないマスの集合
knight_move = [
    (2, 1),
    (1, 2),
    (-1, 2),
    (-2, 1),
    (-2, -1),
    (-1, -2),
    (1, -2),
    (2, -1),
]  # コマの動く先
for i in range(M):
    x, y = map(int, input().split())
    bad_cell.add((x, y))
    for dx, dy in knight_move:
        # 取れる先が存在するマスなら
        if 1 <= x + dx <= N and 1 <= y + dy <= N:
            bad_cell.add((x + dx, y + dy))
# マス全体から置けないマスを引いたものが答え
print(N**2 - len(bad_cell))


# ユーザ解説 (実装量を軽くした版)
n, m = map(int, input().split())
s = set()
for _ in range(m):
    a, b = map(int, input().split())
    s.add((a, b))
    for i in [-1, 1]:
        for j in [-2, 2]:
            s.add((a + i, b + j))
            s.add((a + j, b + i))
ans = n * n
for i, j in s:
    if 1 <= i <= n and 1 <= j <= n:
        ans -= 1
print(ans)
