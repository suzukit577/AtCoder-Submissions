S = sorted(input())
print("Yes" if S == list("ABC") else "No")


# 公式解説-1 (あり得る答えを全て試す)
S = input()
if S in ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]:
    print("Yes")
else:
    print("No")


# 公式解説-2 (条件をより簡単にする)
S = input()
if "A" in S and "B" in S and "C" in S:
    print("Yes")
else:
    print("No")
