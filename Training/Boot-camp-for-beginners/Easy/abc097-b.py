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


X = int(input())
ans = 1
for i in range(X, 0, -1):
    pf = prime_factorization(i)
    if (pf[0][0] == pf[0][1] == 1 and len(pf) == 1) or (
        pf[0][1] > 1 and all(bp[1] == pf[0][1] for bp in pf)
    ):
        print(i)
        break


# ユーザ解説
X = int(input())
ans = 1
for b in range(2, X + 1):
    x = b**2
    while x <= X:
        ans = max(ans, x)
        x *= b
print(ans)
