N, A, B = map(int, input().split())
S = input()
ans = []
num_yes = 0
num_yes_abroad = 0

for i in range(N):
    if S[i] == 'a':
        if num_yes < A + B:
            num_yes += 1
            ans.append('Yes')
        else:
            ans.append('No')
    if S[i] == 'b':
        if num_yes < A + B and num_yes_abroad < B:
            num_yes += 1
            num_yes_abroad += 1
            ans.append('Yes')
        else:
            ans.append('No')
    if S[i] == 'c':
        ans.append('No')
for result in ans:
    print(result)