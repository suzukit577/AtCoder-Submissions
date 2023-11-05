def is_match(s: str) -> bool:
    s1 = "HDCS"
    s2 = "A23456789TJQK"
    return s[0] not in s1 or s[1] not in s2

n = int(input())
s = [input() for i in range(n)]
ans = True
for i in range(n):
    if is_match(s[i]):
        ans = False
for i in range(n-1):
    for j in range(i+1, n):
        if s[i] == s[j]:
            ans = False
if ans:
    print("Yes")
else:
    print("No")