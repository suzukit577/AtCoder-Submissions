s = input()
flag = True
b = []
r = []
k = 0
for i in range(len(s)):
    if s[i] == "B":
        b.append(i)
    if s[i] == "R":
        r.append(i)
    if s[i] == "K":
        k = i
if (b[1] - b[0]) % 2 == 0 or k <= r[0] or r[1] <= k:
    flag = False
print("Yes" if flag else "No")

# 解説
s = input()
c1 = (s.rfind("B") - s.find("B")) % 2 == 1
c2 = s.find("R") < s.find("K") < s.rfind("R")
print("Yes" if c1 and c2 else "No")