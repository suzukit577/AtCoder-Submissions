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
