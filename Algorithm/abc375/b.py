from math import sqrt

N = int(input())
X, Y = [0] * N, [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
ans = sqrt(X[0] ** 2 + Y[0] ** 2)
for i in range(N - 1):
    ans += sqrt((X[i + 1] - X[i]) ** 2 + (Y[i + 1] - Y[i]) ** 2)
ans += sqrt(X[-1] ** 2 + Y[-1] ** 2)
print(ans)


# 公式解説
import math

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
points = [(0, 0)] + points + [(0, 0)]
ans = 0
for i in range(N + 1):
    px, py = points[i]
    qx, qy = points[i + 1]
    ans += math.hypot(px - qx, py - qy)
print(ans)
