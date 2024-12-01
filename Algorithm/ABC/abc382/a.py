N, D = map(int, input().split())
S = input()
print(min(len(S), S.count(".") + D))


# 公式解説
N, D = map(int, input().split())
S = input()
a = 0
for s in S:
    if s == "@":
        a += 1
print(N - a + D)
