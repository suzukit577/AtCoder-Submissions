N = int(input())
A = [list(input()) for _ in range(N)]
a = A[0][:N - 1]
b = [A[i][N - 1] for i in range(N - 1)]
c = A[N - 1][1:]
d = [A[i][0] for i in range(1, N)]
A[0][1:] = a
for i in range(N - 1):
    A[i + 1][N - 1] = b[i]
A[N - 1][:N - 1] = c
for i in range(N - 1):
    A[i][0] = d[i]
for i in range(N):
    print(''.join(A[i]))

# 公式解説
N = int(input())
A = [[0] * N for _ in range(N)]
for i in range(N):
    s = input()
    for j in range(N):
        A[i][j] = int(s[j])
ans = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == 0 or j == 0 or i == N - 1 or j == N - 1:
            if i == 0 and j < N - 1:
                ans[i][j + 1] = A[i][j]
            if i < N - 1 and j == N - 1:
                ans[i + 1][j] = A[i][j]
            if i == N - 1 and j > 0:
                ans[i][j - 1] = A[i][j]
            if i > 0 and j == 0:
                ans[i - 1][j] = A[i][j]
        else:
            ans[i][j] = A[i][j]
for i in range(N):
    print(''.join(map(str, ans[i])))