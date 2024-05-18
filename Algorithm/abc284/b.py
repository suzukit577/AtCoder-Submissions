t = int(input())
N = []
A = []
for i in range(t):
    n = int(input())
    N.append(n)
    a = list(map(int, input().split()))
    A.append(a)
for i in range(t):
    cnt = 0
    for j in range(N[i]):
        if A[i][j] % 2 != 0:
            cnt += 1
    print(cnt)