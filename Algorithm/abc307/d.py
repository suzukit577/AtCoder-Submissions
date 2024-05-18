N = int(input())
S = input()
ans = []
stack = []
for i in range(N):
    ans.append(S[i])
    if S[i] == '(':
        stack.append(len(ans) - 1)
    elif stack and S[i] == ')':
        l = stack.pop()
        ans[l:] = []
print(''.join(ans))