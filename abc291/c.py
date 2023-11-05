import sys

n = int(input())
s = input()
x = 0
y = 0
used = set()
used.add((0,0))
for i in range(n):
    if s[i] == "R":
        x += 1
    if s[i] == "L":
        x -= 1
    if s[i] == "U":
        y += 1
    if s[i] == "D":
        y -= 1
    if (x, y) in used:
        print("Yes")
        sys.exit()
    used.add((x, y))
print("No")