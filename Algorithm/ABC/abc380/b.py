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


# 公式解説 - 解法1: 文字列を辿って解析する
S = input()
A, c = [], 0
for i in range(1, len(S)):
    if S[i] == "-":
        c += 1
    else:
        A.append(c)
        c = 0
print(*A)


# 公式解説 - 解法2: "|" の位置から解析する
S = input()
X = []
for i in range(len(S)):
    if S[i] == "|":
        X.append(i)
print(*[X[i] - X[i - 1] - 1 for i in range(1, len(X))])


# evima 解説
print(*list(map(len, input().split("|")[1:-1])))
