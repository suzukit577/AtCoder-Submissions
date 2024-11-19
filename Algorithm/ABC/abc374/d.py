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
from math import sqrt
from itertools import permutations


def dist(l: tuple[int, int], r: tuple[int, int]) -> float:
    return sqrt((l[0] - r[0]) ** 2 + (l[1] - r[1]) ** 2)


N, S, T = map(int, input().split())
X, Y = [], []  # X[i]: 線分 i の端点, Y[i]: 線分 i のもう一方の端点
for _ in range(N):
    A, B, C, D = map(int, input().split())
    X.append((A, B))
    Y.append((C, D))
res = 10**18
for p in permutations(range(N)):
    for mask in range(1 << N):
        cur_res, cur_point = 0, (0, 0)
        for i in range(N):
            if mask & (1 << i):
                cur_res += dist(cur_point, X[p[i]]) / S
                cur_res += dist(X[p[i]], Y[p[i]]) / T
                cur_point = Y[p[i]]
            else:
                cur_res += dist(cur_point, Y[p[i]]) / S
                cur_res += dist(Y[p[i]], X[p[i]]) / T
                cur_point = X[p[i]]
        res = min(res, cur_res)
print(res)

# ユーザ解説 (計算量の改善)
"""
- 各頂点  (A_i, B_i), (C_i, D_i), (0, 0) の座標を適当にラベリングし、頂点 0, 1, ..., 2N とする
- dp[S][j]: 既に引いた線分の集合を S としたときの、現在いる頂点が j であるような引き方のうちの最短時間
- TSP と同じ bitDP で解ける
-> 時間計算量: O(N^2 x 2^N)
"""
from math import sqrt

N, S, T = map(int, input().split())
X, Y = (
    [0] * (2 * N + 1),
    [0] * (2 * N + 1),
)  # X[i]: 頂点 i の x 座標, Y[i]: 頂点 i の y 座標
for i in range(N):
    X[2 * i], Y[2 * i], X[2 * i + 1], Y[2 * i + 1] = map(int, input().split())
dist = [[0] * (2 * N + 1) for _ in range(2 * N + 1)]
for i in range(2 * N + 1):
    for j in range(2 * N + 1):
        dist[i][j] = sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
INF = 1 << 30
dp = [[INF] * (2 * N + 1) for _ in range(1 << N)]
dp[0][2 * N] = 0
for mask in range(1 << N):
    for i in range(2 * N + 1):
        if dp[mask][i] != INF:
            for j in range(N):
                if not mask & (1 << j):
                    for c in range(2):
                        a = j * 2 + c
                        b = j * 2 + 1 - c
                        dp[mask + (1 << j)][b] = min(
                            dp[mask + (1 << j)][b],
                            dp[mask][i] + dist[i][a] / S + dist[a][b] / T,
                        )
ans = INF
for i in range(2 * N + 1):
    ans = min(ans, dp[(1 << N) - 1][i])
print(ans)
