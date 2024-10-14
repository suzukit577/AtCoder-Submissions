N = int(input())
A = [list(input()) for _ in range(N)]
ans = [[""] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        k = min(i, j, N - 1 - i, N - 1 - j)
        if k % 4 == 0:
            new_i, new_j = j, N - 1 - i  # 90 度回転
        elif k % 4 == 1:
            new_i, new_j = N - 1 - i, N - 1 - j  # 180 度回転
        elif k % 4 == 2:
            new_i, new_j = N - 1 - j, i  # 270 度回転
        else:
            new_i, new_j = i, j  # 回転させない
        ans[new_i][new_j] = A[i][j]
for a in ans:
    print("".join(a))


# 公式解説
N = int(input())
A = [list(input()) for _ in range(N)]
ans = [[""] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        d = min(i + 1, j + 1, N - i, N - j)
        ni, nj = i, j
        for _ in range(d % 4):
            ti, tj = nj, N - 1 - ni
            ni, nj = ti, tj
        ans[ni][nj] = A[i][j]
for a in ans:
    print("".join(a))
