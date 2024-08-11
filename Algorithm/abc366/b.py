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
