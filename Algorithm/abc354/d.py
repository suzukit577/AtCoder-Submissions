A, B, C, D = map(int, input().split())
x_origin, y_origin = A % 4, B % 4
width, height = C - A, D - B

# evima 解説 (二次元累積和)
def f(y: int, x: int) -> int:
    a = [[0, 0, 0, 0, 0],
        [0, 2, 3, 3, 4],
        [0, 3, 6, 7, 8]]
    sub1 = (y // 2) * (x // 4) * a[2][4]
    sub2 = (y // 2) * a[2][x % 4]
    sub3 = (x // 4) * a[y % 2][4]
    sub4 = a[y % 2][x % 4]
    return sub1 + sub2 + sub3 + sub4

M = 10 ** 9
A, B, C, D = map(lambda x: int(x) + M, input().split())
print(f(D, C) - f(D, A) - f(B, C) + f(B, A))

# 公式解説
mass = [
    [2, 1, 0, 1],
    [1, 2, 1, 0]
]
INF = 10 ** 9

A, B, C, D = map(int, input().split())
ans = 0
for fy in range(2):
    for fx in range(4):
        x1, x2 = (A - fx + 3 + INF) // 4, (C - fx + 3 + INF) // 4
        y1, y2 = (B - fy + 1 + INF) // 2, (D - fy + 1 + INF) // 2
        ans += (x2 - x1) * (y2 - y1) * mass[fy][fx]
print(ans)