N = int(input())
S = [input() for _ in range(N)]
cnt = 0
for i in range(N):
    if S[i] == "For":
        cnt += 1
print("Yes" if cnt > N // 2 else "No")