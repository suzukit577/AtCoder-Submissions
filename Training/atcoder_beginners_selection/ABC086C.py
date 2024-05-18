n = int(input())
t, x, y = (n+1) * [0], (n+1) * [0], (n+1) * [0]
for i in range(n):
    t[i+1], x[i+1], y[i+1] = map(int, input().split())

can = True
for i in range(n):
    dt = t[i+1] - t[i]
    dist = abs(x[i+1] - x[i]) + abs(y[i+1] - y[i])
    if dt < dist:
        can = False
    if dt % 2 != dist % 2:
        can = False # dt と dist の偶奇は一致する必要あり

if can:
    print("Yes")
else:
    print("No")