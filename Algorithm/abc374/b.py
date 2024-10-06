S, T = input(), input()
if S == T:
    print(0)
else:
    for i in range(min(len(S), len(T))):
        if S[i] != T[i]:
            print(i + 1)
            break
    else:
        print(min(len(S), len(T)) + 1)
