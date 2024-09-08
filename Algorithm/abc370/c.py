# コンテスト中の提出: O(N^2)
S, T = list(input().strip()), list(input().strip())
N = len(S)
X = []
for i in range(N):
    if S[i] > T[i]:
        S[i] = T[i]
        X.append("".join(S))
for i in range(N - 1, -1, -1):
    if S[i] < T[i]:
        S[i] = T[i]
        X.append("".join(S))
print(len(X))
for x in X:
    print(x)

# evima 解説: O(N^3)
S, T = input(), input()
N = len(S)
X = []
while S != T:
    nS = "z" * N
    for i in range(N):
        if S[i] != T[i]:
            nS = min(nS, S[:i] + T[i] + S[i + 1 :])
    X.append(nS)
    S = nS
print(len(X))
for x in X:
    print(x)
