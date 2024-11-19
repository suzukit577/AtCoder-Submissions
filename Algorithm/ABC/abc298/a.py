# 提出コード
n = int(input())
s = input()
print("Yes" if "o" in s and "x" not in s else "No")

# 公式解説
n = int(input())
s = input()
f1 = False # "o" が少なくとも1人いる
f2 = True # "x" が1人もいない
for i in range(n):
    if s[i] == "o":
        f1 = True
    if s[i] == "x":
        f2 = False
print("Yes" if f1 and f2 else "No")