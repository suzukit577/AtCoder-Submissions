# ans-1
n = int(input())
s = list(input())
while True:
    fin = 1
    for i in range(len(s)-1):
        if s[i] == "n" and s[i+1] == "a":
            s.insert(i+1, "y")
            fin = 0
            break
    if fin:
        break
print("".join(s))

# ans-2
n = int(input())
s = list(input())
ans = []
for i in range(n):
    if i >= 1 and ans[-1] == "n" and s[i] == "a":
        ans.append("y")
    ans.append(s[i])
print("".join(ans))

# ans-3
n = int(input())
s = input()
print(s.replace("na", "nya"))
