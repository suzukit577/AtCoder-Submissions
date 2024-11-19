S, T = input(), input()
if S == T:
    print(0)
else:
    N = min(len(S), len(T))
    for i in range(N):
        if S[i] != T[i]:
            print(i + 1)
            break
    else:
        print(N + 1)

# 公式解説
S, T = input(), input()
N = min(len(S), len(T))
if S == T:
    print(0)
elif S[:N] == T[:N]:
    print(N + 1)
else:
    for i in range(N):
        if S[i] != T[i]:
            print(i + 1)
            break
