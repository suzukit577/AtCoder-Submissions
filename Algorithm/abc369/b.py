N = int(input())
ans = 0
AL, AR, SL, SR = [], [], [], []
for _ in range(N):
    A, S = input().split()
    A = int(A)
    if S == "L":
        AL.append(A)
        SL.append(S)
    else:
        AR.append(A)
        SR.append(S)
for i in range(1, len(AL)):
    ans += abs(AL[i] - AL[i - 1])
for i in range(1, len(AR)):
    ans += abs(AR[i] - AR[i - 1])
print(ans)
