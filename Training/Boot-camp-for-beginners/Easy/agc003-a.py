S = set(input())
flag = True
if "N" in S and "S" not in S:
    flag = False
if "N" not in S and "S" in S:
    flag = False
if "W" in S and "E" not in S:
    flag = False
if "W" not in S and "E" in S:
    flag = False
print("Yes" if flag else "No")
