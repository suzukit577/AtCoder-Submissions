n = int(input())
s = input()
flag = True
for i in range(n-1):
    if s[i] == "M" and s[i+1] == "M":
        flag = False
    elif s[i] == "F" and s[i+1] == "F":
        flag = False
print("Yes" if flag else "No")

# 解説
n = int(input())
s = input()
for i in range(n-1):
    if s[i] == s[i+1]:
        print("No")
        exit()
print("Yes")