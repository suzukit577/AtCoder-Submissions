from itertools import permutations

N, M = map(int, input().split())
S = [input() for _ in range(N)]
permS = list(permutations(S))
flag = False
for s in permS:
    for i in range(N - 1):
        diff = 0
        for j in range(M):
            if s[i][j] != s[i+1][j]:
                diff += 1
        if diff != 1:
            break
    else:
        flag = True
        break
print('Yes' if flag else 'No')

# 公式解説
from itertools import permutations

N, M = map(int, input().split())
S = [input() for _ in range(N)]
S.sort()
for s in list(permutations(S)):
    ok = True
    for i in range(N-1):
        cnt = 0
        for j in range(M):
            if s[i][j] != s[i+1][j]:
                cnt += 1
        if cnt != 1:
            ok = False
    if ok:
        print('Yes')
        exit()
print('No')