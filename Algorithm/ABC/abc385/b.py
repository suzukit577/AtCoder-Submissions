H, W, X, Y = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = input()
houses = set()
i, j = X - 1, Y - 1
if S[i][j] == "@":
    houses.add((i, j))
for t in T:
    if t == "U" and 0 <= i - 1 <= H - 1 and S[i - 1][j] != "#":
        i -= 1
    if t == "D" and 0 <= i + 1 <= H - 1 and S[i + 1][j] != "#":
        i += 1
    if t == "L" and 0 <= j - 1 <= W - 1 and S[i][j - 1] != "#":
        j -= 1
    if t == "R" and 0 <= j + 1 <= W - 1 and S[i][j + 1] != "#":
        j += 1
    if S[i][j] == "@":
        houses.add((i, j))
print(i + 1, j + 1, len(houses))
