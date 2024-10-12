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
min_move_len = 10**20
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
        min_move_len = min(min_move_len, move_len)
print(segment_len / T + min_move_len / S)


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
min_move_len = 10**20
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
        min_move_len = min(min_move_len, move_len)
print(segment_len / T + min_move_len / S)


# 公式解説
"""
- 線分を描く順序: N! 通り
- 線分を描く向き (どちらの点からどちらの点へと描くか): 2^N 通り
-> 全探索の時間計算量: O(N! x 2^N)
"""
# write code here


# ユーザ解説 (計算量の改善)
"""
- 各点の座標を適当にラベリングし、頂点 0, 1, ..., 2N とする
- dp[S][j] を、既に引いた線分の集合を S としたときの今いる頂点が j であるような引き方のうちの最短時間とする
- TSP と同じ bitDP で解ける
-> 時間計算量: O(N^2 x 2^N)
"""
# write code here
