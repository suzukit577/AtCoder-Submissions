# evima 解説
N, M, K = map(int, input().split())
C, A, R = [], [], []
for _ in range(M):
    CAR = list(input().split())
    C.append(int(CAR[0]))
    A.append(list(map(int, CAR[1:-1])))
    R.append(CAR[-1])

ans = 0
for mask in range(1 << N):  # 0 の桁は偽物，1 の桁は本物
    ok = True
    for i in range(M):  # テスト結果確認
        cnt_genuine = 0
        for a in A[i]:
            cnt_genuine += (mask >> (a - 1)) & 1
        ok &= (cnt_genuine >= K) == (R[i] == "o")
    ans += ok
print(ans)
