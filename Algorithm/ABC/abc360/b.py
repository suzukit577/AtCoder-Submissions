S, T = input().split()
for w in range(1, len(S)):
    words = [S[i : i + w] for i in range(0, len(S), w)]
    for c in range(1, w + 1):
        ans = ""
        for word in words:
            if len(word) >= c:
                ans += word[c - 1]
        if ans == T:
            print("Yes")
            exit()
print("No")

# evima 解説
S, T = input().split()
for w in range(1, len(S)):
    for c in range(w):
        l = []
        for i in range(c, len(S), w):
            l.append(S[i])
        if "".join(l) == T:
            print("Yes")
            exit()
print("No")
