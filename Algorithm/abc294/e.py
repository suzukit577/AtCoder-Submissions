L, N1, N2 = map(int, input().split())
x1 = []; x2 = []
for _ in range(N1):
    v, l = map(int, input().split())
    x1 += [v] * l
for _ in range(N2):
    v, l = map(int, input().split())
    x2 += [v] * l