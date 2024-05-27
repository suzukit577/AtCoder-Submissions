H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
ans = [[""] * W for _ in range(2 * H)]
for i in range(H):
    for j in range(W):
        ans[2 * i][j] = C[i][j]
        ans[2 * i + 1][j] = C[i][j]
for i in range(2 * H):
    for j in range(W):
        print(ans[i][j], end="")
    print()

# 別解
H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
for i in range(2 * H):
    for j in range(W):
        print(C[i // 2][j], end="")
    print()
