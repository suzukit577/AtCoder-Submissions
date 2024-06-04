S = input()
K = int(input())
for i in range(len(S)):
    num = int(S[i])
    if num != 1 and i < K:
        print(num)
        break
else:
    print(1)

# 公式解説
S = input()
K = int(input())
for i in range(min(len(S), K)):
    if S[i] >= "2":
        print(S[i])
        break
else:
    print("1")
