# 公式解説
## ソートのキーを渡す方法
from functools import cmp_to_key

def cmp(a, b):
    x, y, i = a
    xx, yy, ii = b
    s = x * yy - y * xx
    return 1 if s > 0 else -1 if s < 0 else 0

N = int(input())
X = []
for i in range(N):
    a, b = map(int, input().split())
    X.append((-a, a + b, i))

X.sort(key = cmp_to_key(cmp))
print(*[i + 1 for x, y, i in X])

## 精度を上げて比較する方法
### 多倍長整数を使う方法
#### タプルを保持 (10 ** 100 を掛けて比較)
N = int(input())
X = []
for i in range(N):
    a, b = map(int, input().split())
    X.append((-a * 10 ** 100 // (a + b), i))
X.sort() # key 指定なしだと, tuple の 0 番目の要素で大小比較
print(*[i + 1 for x, i in X])

#### 一次元化 (10 ** 100 を掛けて比較, 一次元化)
N = int(input())
X = []
for i in range(N):
    a, b = map(int, input().split())
    X.append((-a * 10 ** 100 // (a + b)) * 10 ** 6 + i)
X.sort()
print(*[x % 10 ** 6 + 1 for x in X])

### Decimal を使う方法
#### 入力を Decimal で受け取ると浮動小数点数より精度を上げることができる．
#### ただし，Decimal は PyPy では遅くなるので TLE に注意する．
from decimal import Decimal, getcontext

getcontext().prec = 100
N = int(input())
X = []
for i in range(N):
    a, b = map(Decimal, input().split())
    X.append((-a / (a + b), i))
X.sort()
print(*[i + 1 for x, i in X])

## 10^18 以下に埋め込む方法
"""
'a / (a + b)' のソートは，逆数にして 1 を引くことで b / a のソートと等価になる．
これにはいくつかの方法が知られているが，商が 1 より大きいか小さいかで場合分けすることで，0 <= a, b <= 10 ** 9 のとき，商を -10^18 から 10^18 程度の区間に (順序を保って) 自然に埋め込むことができる．
なお，途中計算で O(N) 回程度 10^18 を超える整数を扱う必要があるが，比較の際には 64 bit に収まっているので，実行時間のボトルネックにはなりづらい．
"""
def f(i):
    a, b = X[i]
    if b == 0:
        return -M - 1
    if a == 0:
        return M + 1
    if b > a:
        return M - a * M // b
    return b * M // a - M

M = 10 ** 18
N = int(input())
X = []
for i in range(N):
    a, b = map(int, input().split())
    X.append((a, b))
L = [i for i in range(N)]
L.sort(key = f)
print(*[i + 1 for i in L])

# 公式解説の Python での実装例
class Frac:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

N = int(input())
A, B = [0], [0]
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
l = sorted(range(1, N + 1), key=lambda i: Frac(-A[i], A[i] + B[i]))
print(' '.join(map(str, l)))

# 10^20 を掛けると通ること
from collections import defaultdict

N = int(input())
dd = defaultdict(list)
for i in range(N):
    A, B = map(int, input().split())
    success_rate = (10 ** 20) * A // (A + B) # Python は多倍長整数が扱える -> 精度が上がる
    dd[success_rate].append(i + 1)
success_rate_desc = sorted(dd.keys(), reverse=True)
ans = []
for rate in success_rate_desc:
    ans += sorted(dd[rate])
print(*ans)