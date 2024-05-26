def prime_factorization(n):
    """
    - 2以上の自然数nを素因数分解する関数
    - 計算量: O(√n)
    - 入力: n
    - 出力: [[素因数, 指数], ...]の2次元リスト
    """
    arr = []
    tmp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if tmp % i == 0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            arr.append([i, cnt])
    if tmp != 1:
        arr.append([tmp, 1])
    if not arr:
        arr.append([n, 1])
    return arr


N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        dist = 0
        for k in range(D):
            dist += (X[i][k] - X[j][k]) ** 2
        for p, d in prime_factorization(dist):
            if p != 1 and d % 2 != 0:
                break
        else:
            ans += 1
print(ans)
