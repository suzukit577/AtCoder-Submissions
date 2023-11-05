from collections import defaultdict

n, q = map(int, input().split())
d = defaultdict(int)
for _ in range(q):
    c, x = input().split()
    if c == "1":
        d[x] += 1
    if c == "2":
        d[x] += 2
    if c == "3":
        if d[x] >= 2:
            print("Yes")
        else:
            print("No")