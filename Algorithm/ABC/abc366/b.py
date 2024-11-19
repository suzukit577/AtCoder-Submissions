from typing import Any


def rotate_matrix(Mat: list[list[Any]]) -> list[list[Any]]:
    """clockwise rotation of given matrix: O(n^2)

    Args:
        Mat (list): 2D list (matrix)

    Returns:
        list: clockwise rotation of given 2D list (clockwise rotation of given matrix)
    """
    return [list(a)[::-1] for a in zip(*Mat)]


N = int(input())
S = [list(input()) for _ in range(N)]
M = max(list(map(len, S)))
for s in S:
    if len(s) < M:
        for _ in range(M - len(s)):
            s.append("*")
S = rotate_matrix(S)
for i in range(M):
    for j in range(N - 1, 0, -1):
        if S[i][j] == "*":
            S[i][j] = ""
        else:
            break
for s in S:
    print("".join(s))


# evima 解説
N = int(input())
S = [input() for _ in range(N)]

M = max(len(s) for s in S)
for i in range(N):
    S[i] += "*" * (M - len(S[i]))

T = [list(z)[::-1] for z in zip(*S)]
for t in T:
    while t[-1] == "*":
        t.pop()
    print("".join(t))


# 公式解説
N = int(input())
S = [input() for _ in range(N)]
M = max(map(len, S))
T = [["*"] * N for _ in range(M)]
for i in range(N):
    for j in range(len(S[i])):
        T[j][N - i - 1] = S[i][j]
for i in range(M):
    while T[i][-1] == "*":
        T[i].pop()
    print("".join(T[i]))
