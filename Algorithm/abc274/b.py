def count_box(lst):
    cnt = 0
    for i in range(len(lst)):
        if lst[i] == '#':
            cnt += 1
    return cnt

h, w = map(int, input().split())
c = [input() for _ in range(h)]
ct = [[None] * h for _ in range(w)]
for i in range(h):
    for j in range(w):
        ct[j][i] = c[i][j]
x = [count_box(ct[i]) for i in range(w)]
print(*x)