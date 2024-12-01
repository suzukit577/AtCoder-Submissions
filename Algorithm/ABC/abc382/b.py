N, D = map(int, input().split())
S = list(input())
cnt = 0
for i in range(N - 1, -1, -1):
    if cnt < D and S[i] == "@":
        S[i] = "."
        cnt += 1
print("".join(S))


# 公式解説
N, D = map(int, input().split())
S = input()
for i in range(D):
    for j in range(N):
        if S[N - 1 - j] == "@":
            S = S[: N - 1 - j] + "." + S[N - j :]
            break
print(S)
