# Original
from itertools import permutations
from math import sqrt

N, S, T = map(int, input().split())
start_points, end_points = [], []
for _ in range(N):
    A, B, C, D = map(int, input().split())
    start_points.append((A, B))
    end_points.append((C, D))
points = [start_points, end_points]
segment_len = sum(
    sqrt((s[0] - e[0]) ** 2 + (s[1] - e[1]) ** 2)
    for s, e in zip(start_points, end_points)
)
optim_move_len = 10**20
for p in permutations(range(N)):
    for mask in range(1 << N):
        move_len = 0
        if mask & 1:
            move_len += sqrt(points[0][p[0]][0] ** 2 + points[0][p[0]][1] ** 2)
        else:
            move_len += sqrt(points[1][p[0]][0] ** 2 + points[1][p[0]][1] ** 2)
        for i in range(N - 1):
            s = 1 if mask & (1 << i) else 0
            e = 0 if mask & (1 << (i + 1)) else 1
            move_len += sqrt(
                (points[s][p[i]][0] - points[e][p[i + 1]][0]) ** 2
                + (points[s][p[i]][1] - points[e][p[i + 1]][1]) ** 2
            )
        optim_move_len = min(optim_move_len, move_len)
print(segment_len / T + optim_move_len / S)


# Refactoring by ChatGPT
from itertools import permutations
from math import sqrt

N, S, T = map(int, input().split())
start_points, end_points = [], []
for _ in range(N):
    A, B, C, D = map(int, input().split())
    start_points.append((A, B))
    end_points.append((C, D))
segment_len = sum(
    sqrt((s[0] - e[0]) ** 2 + (s[1] - e[1]) ** 2)
    for s, e in zip(start_points, end_points)
)
optim_move_len = 10**20
for p in permutations(range(N)):
    for mask in range(1 << N):
        move_len = 0
        if mask & 1:
            move_len += sqrt(start_points[p[0]][0] ** 2 + start_points[p[0]][1] ** 2)
            prev_end = end_points[p[0]]
        else:
            move_len += sqrt(end_points[p[0]][0] ** 2 + end_points[p[0]][1] ** 2)
            prev_end = start_points[p[0]]
        for i in range(1, N):
            if (mask >> i) & 1:
                move_len += sqrt(
                    (prev_end[0] - start_points[p[i]][0]) ** 2
                    + (prev_end[1] - start_points[p[i]][1]) ** 2
                )
                prev_end = end_points[p[i]]
            else:
                move_len += sqrt(
                    (prev_end[0] - end_points[p[i]][0]) ** 2
                    + (prev_end[1] - end_points[p[i]][1]) ** 2
                )
                prev_end = start_points[p[i]]
        optim_move_len = min(optim_move_len, move_len)
print(segment_len / T + optim_move_len / S)
