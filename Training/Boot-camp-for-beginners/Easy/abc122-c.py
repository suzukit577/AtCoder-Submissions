S = input()
ans = 0
for i in range(10):
    for j in range(len(S) - i):
        if set(S[j : j + i + 1]) <= set(["A", "C", "G", "T"]):
            ans = len(S[j : j + i + 1])
            break
print(ans)
