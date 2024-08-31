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

# 公式解説
N = int(input())
pos = [-1, -1]  # 0: left, 1: right
ans = 0
for i in range(N):
    A, S = input().split()
    A = int(A)
    hand = 0 if S == "L" else 1
    if pos[hand] != -1:
        ans += abs(pos[hand] - A)
    pos[hand] = A
print(ans)

# evima 解説
N = int(input())
l, r, ans = -1, -1, 0
for _ in range(N):
    A, S = input().split()
    A = int(A)
    if S == "L":
        if l != -1:
            ans += abs(A - l)
        l = A
    else:
        if r != -1:
            ans += abs(A - r)
        r = A
print(ans)
