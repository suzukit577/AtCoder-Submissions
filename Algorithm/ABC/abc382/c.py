# 公式解説: O(N + M + max(B))
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
K = 2 * 10**5 + 1  # B の上界
idx = [-1] * K
r = K
for i in range(N):
    while r > A[i]:
        r -= 1
        idx[r] = i + 1
for b in B:
    print(idx[b])


# ユーザ解説 - 二分探索を用いた解法 by AngrySadEight: Θ(M log N)
from bisect import bisect_right

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [A[0]] * N
for i in range(1, N):
    C[i] = min(A[i], C[i - 1])
C = C[::-1]
for b in B:  # O(M)
    idx = bisect_right(C, b)  # O(log N)
    print(-1 if idx == 0 else N - bisect_right(C, b) + 1)
