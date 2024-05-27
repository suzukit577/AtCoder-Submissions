S = input()
T = input()
N = len(S)
S *= 2
for i in range(N):
    if S[i : i + N] == T:
        print("Yes")
        break
else:
    print("No")

# 公式解説, ユーザ解説
S = input()
T = input()
N = len(S)
ans = False
for i in range(N):
    if S == T:
        ans = True
        break
    S = S[-1] + S[0:-1]
print("Yes" if ans else "No")
