from itertools import combinations

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
comb = set(combinations(A[0], 2))
for i in range(M):
    for j in range(N-1):
        comb.discard((A[i][j], A[i][j + 1]))
        comb.discard((A[i][j + 1], A[i][j]))
print(len(comb))


# 公式解説
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
ans = 0
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        flag = False
        for k in range(M):
            for l in range(N - 1):
                if A[k][l] == i and A[k][l + 1] == j:
                    flag = True
                if A[k][l] == j and A[k][l + 1] == i:
                    flag = True
        if not flag:
            ans += 1
print(ans)