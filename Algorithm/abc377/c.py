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
