H, W = map(int, input().split())
Si, Sj = map(int, input().split())
Si -= 1
Sj -= 1
C = [list(input()) for _ in range(H)]
X = input()
for x in X:
    if x == "L" and Sj - 1 >= 0 and C[Si][Sj - 1] == ".":
        Sj -= 1
    elif x == "R" and Sj + 1 < W and C[Si][Sj + 1] == ".":
        Sj += 1
    elif x == "U" and Si - 1 >= 0 and C[Si - 1][Sj] == ".":
        Si -= 1
    elif x == "D" and Si + 1 < H and C[Si + 1][Sj] == ".":
        Si += 1
print(Si + 1, Sj + 1)

# evima 解説
H, W = map(int, input().split())
Si, Sj = map(int, input().split())
C = [input() for _ in range(H)]
X = input()
y, x = Si - 1, Sj - 1
for c in X:
    if c == "L" and x > 0 and C[y][x - 1] != "#":
        x -= 1
    if c == "R" and x < W - 1 and C[y][x + 1] != "#":
        x += 1
    if c == "U" and y > 0 and C[y - 1][x] != "#":
        y -= 1
    if c == "D" and y < H - 1 and C[y + 1][x] != "#":
        y += 1
print(y + 1, x + 1)
