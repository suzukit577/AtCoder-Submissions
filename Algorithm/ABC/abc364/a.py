N = int(input())
S = [input() for _ in range(N)]
for i in range(N - 2):
    if S[i] == S[i + 1] == "sweet":
        print("No")
        break
else:
    print("Yes")

# evima 解説
N = int(input())
S = [input() for _ in range(N)]
ans = True
for i in range(N - 2):
    if S[i] == S[i + 1] == "sweet":
        ans = False
print("Yes" if ans else "No")
