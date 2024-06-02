# evima 解説
N, M, K = map(int, input().split())
C, A, R = [], [], []
for _ in range(M):
    CAR = list(input().split())
    C.append(int(CAR[0]))
    A.append(list(map(int, CAR[1:-1])))
    R.append(CAR[-1])

ans = 0
for mask in range(1 << N):
    ok = True
    for i in range(M):
        cnt = 0
        for a in A[i]:
            cnt += (mask >> (a - 1)) & 1
        ok &= (cnt >= K) == (R[i] == "o")
    ans += ok
print(ans)
