N = int(input())
S = input()
t = S.count('T')
a = S.count('A')
if t > a:
    print('T')
elif a > t:
    print('A')
else:
    tt = 0; aa = 0
    for i in range(N):
        if S[i] == 'T':
            tt += 1
        if S[i] == 'A':
            aa += 1
        if tt == t:
            print('T')
            exit()
        if aa == a:
            print('A')
            exit()

# 公式解説
N = int(input())
S = input()
t = 0
a = 0
for i in range(N):
    if S[i] == 'T':
        t += 1
    else:
        a += 1
if t > a:
    print('T')
elif t < a:
    print('A')
elif S[-1] == 'A':
    print('T')
else:
    print('A')

# ユーザー解説
N = int(input())
S = input()
t = 0
a = 0
for s in S:
    if s == 'T':
        t += 1
    if s == 'A':
        a += 1
    if t == (N + 1) // 2:
        print('T')
        exit()
    if a == (N + 1) // 2:
        print('A')
        exit()