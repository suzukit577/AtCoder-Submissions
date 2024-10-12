N = int(input())
A = [list(input()) for _ in range(N)]
ans = [["" for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        k = min(i, j, N - 1 - i, N - 1 - j)
        rotation = (k % 4) + 1  # 回転回数
        if rotation == 1:  # 90 度回転
            new_i, new_j = j, N - 1 - i
        elif rotation == 2:  # 180 度回転
            new_i, new_j = N - 1 - i, N - 1 - j
        elif rotation == 3:  # 270 度回転
            new_i, new_j = N - 1 - j, i
        else:  # 回転させない
            new_i, new_j = i, j
        ans[new_i][new_j] = A[i][j]
for a in ans:
    print("".join(a))
