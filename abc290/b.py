n, k = map(int, input().split())
s = list(input())
cnt = 0
for i in range(len(s)):
    if s[i] == "o":
        cnt += 1
        if cnt > k:
            s[i] = "x"
print("".join(s))