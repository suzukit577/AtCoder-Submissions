from bisect import bisect_left, bisect_right

N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))
CP = [0] * (N + 1)
for i in range(N):
    CP[i + 1] = CP[i] + P[i]
Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    print(CP[bisect_right(X, R)] - CP[bisect_left(X, L)])
