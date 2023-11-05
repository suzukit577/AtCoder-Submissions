n = int(input())
s = input()
id_1 = 0; id_2 = 0; id_3 = 0
for i in range(n):
    if s[i] == "|" and id_1 == 0:
        id_1 = i + 1
    elif s[i] == "|" and id_1 != 0:
        id_2 = i + 1
    elif s[i] == "*":
        id_3 = i + 1
print("in" if id_1 < id_3 < id_2 else "out")

# 公式解説
N = int(input())
S = input()
v_first = s.index("|")
s = S.index("*")
v_second = S.rindex("|")
print("in" if v_first < s < v_second else "out")

# 原案者の実装
import re
N, S = input(), input()
print("in" if re.search("\|.*\*.*\|", S) else "out")