H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]
for i in range(H):
    s = []
    for j in range(W):
        if a[i][j] == 0:
            s.append(".")
        else:
            s.append(chr(ord("A") + a[i][j] - 1))
    print("".join(s))