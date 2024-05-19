S = input()
N = len(S)
X = set()
Y = list()
for i in range(N):
    if S[i] == '(':
        Y.append(set())
    elif ord('a') <= ord(S[i]) <= ord('z'):
        if S[i] in X:
            print('No')
            exit()
        else:
            X.add(S[i])
            if len(Y) != 0:
                Y[-1].add(S[i])
    elif S[i] == ')':
        X -= Y.pop()
print('Yes')