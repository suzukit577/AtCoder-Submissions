K = int(input())

from collections import defaultdict
def prime_factorize(n: int):
    ddict = defaultdict(int)   # key: 素因数, value: 素因数の指数
    arr = []    # 素因数のリスト
    tmp = n
    for i in range(2, int(-((-n ** 0.5)//1))+1):  # 2からsqrt(n)までで素因数を探索
        if tmp % i == 0:
            while tmp % i == 0:
                tmp //= i
                arr.append(i)
                ddict[i] += 1
    if tmp != 1:    # tmpが1でない場合は素因数のリストと辞書にtmpを追加
        arr.append(tmp)
        ddict[tmp] += 1
    if not arr:     # 素因数のリストが空ならnを素因数のリストに追加
        arr.append(n)
        ddict[n] += 1
    return ddict, arr

ddict, fs = prime_factorize(K)
ans = 0
for k, v in ddict.items():
    if v == 1:
        ans = max(ans, k)
        continue
    v2 = 0
    cnt = 0
    tmp = 0
    while v > v2:
        tmp += k
        t = tmp
        while t % k == 0:
            t //= k
            v2 += 1
    ans = max(tmp, ans)
print(ans)