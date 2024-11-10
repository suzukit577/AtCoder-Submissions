N, K = map(int, input().split())
S = input()
ans, i = 0, 0
while i < N:
    if S[i] == "O":
        if i + K <= N and "X" not in S[i : i + K]:
            ans += 1
            i += K
        else:
            i += 1
    else:
        i += 1
print(ans)
