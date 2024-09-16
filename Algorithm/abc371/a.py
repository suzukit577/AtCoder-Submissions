SAB, SAC, SBC = input().split()
if SAB == SAC == "<":
    if SBC == "<":
        print("B")
    else:
        print("C")
elif SAB == SAC == ">":
    if SBC == ">":
        print("B")
    else:
        print("C")
else:
    print("A")

# 別解 (evima 動画コメント)
SAB, SAC, SBC = input().split()
A, B, C = 0, 0, 0
if SAB == ">":
    A += 1
else:
    B += 1
if SAC == ">":
    A += 1
else:
    C += 1
if SBC == ">":
    B += 1
else:
    C += 1
print("A" if A == 1 else "B" if B == 1 else "C")

# evima 解説
AB, AC, BC = input().split()
if AB == "<" and AC == ">" or AB == ">" and AC == "<":
    print("A")
elif AB == "<" and BC == "<" or AB == ">" and BC == ">":
    print("B")
else:
    print("C")
