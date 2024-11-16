S = input()
N = len(S)
A, i = [], 0
while i < N - 1:
    if S[i] == "|":
        cnt = 0
        i += 1
        while S[i] != "|":
            cnt += 1
            i += 1
        A.append(cnt)
print(*A)
