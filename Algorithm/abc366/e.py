# evima 解説
N, D = map(int, input().split())
M = 10**6
x, y = [0] * N, [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())
    x[i] += 2 * M
    y[i] += 2 * M


def f(z: list[int]) -> list[int]:
    c = [0] * (4 * M + 1)
    for v in z:
        c[v] += 1
    s = [0] * (4 * M + 1)
    s[0] = sum(z)
    d = -N
    for i in range(4 * M):
        d += 2 * c[i]
        s[i + 1] = s[i] + d
    return s


sx, sy = f(x), f(y)
cy = [0] * (D + 1)
for v in sy:
    if v <= D:
        cy[v] += 1
a = [0] * (D + 2)
for i in range(D + 1):
    a[i + 1] = a[i] + cy[i]
ans = 0
for v in sx:
    if v <= D:
        ans += a[D - v + 1]
print(ans)


# 公式解説
N, D = map(int, input().split())
x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())
M = 2 * 10**6


def calc(xs: list[int]) -> list[int]:
    xsum = [0] * (2 * M + 1)
    xs.sort()
    i = 0
    xsum[-M] = sum(xs) + N * M
    for x in range(-M + 1, M + 1):
        while i < N and xs[i] < x:
            i += 1
        xsum[x] = xsum[x - 1] + 2 * i - N
    return xsum


xsum = calc(x)
ysum = calc(y)
xsum.sort()
ysum.sort()
ans = 0
j = 0
for i in range(2 * M + 1)[::-1]:
    while j < 2 * M + 1 and xsum[i] + ysum[j] <= D:
        j += 1
    ans += j
print(ans)
