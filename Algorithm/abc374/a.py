S = input()
if S[-3:] == "san":
    print("Yes")
else:
    print("No")

# 別解
S = input()
print("Yes" if S[-3:] == "san" else "No")
