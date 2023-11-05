N = int(input())
if N <= 10 ** 3 - 1:
    print(N)
if 10 ** 3 <= N <= 10 ** 4 - 1:
    print(N // 10 * 10)
if 10 ** 4 <= N <= 10 ** 5 - 1:
    print(N // 100 * 100)
if 10 ** 5 <= N <= 10 ** 6 - 1:
    print(N // 1000 * 1000)
if 10 ** 6 <= N <= 10 ** 7 - 1:
    print(N // 10000 * 10000)
if 10 ** 7 <= N <= 10 ** 8 - 1:
    print(N // 100000 * 100000)
if 10 ** 8 <= N <= 10 ** 9 - 1:
    print(N // 1000000 * 1000000)

# 公式解説
"""
N の 10^d の位を切り捨てることは，
・N を 10^{d+1} で割った余りを M として，N を N - M に置き換える
・N を文字列と捉え，4文字目以降をすべて '0' に置き換える
などというように言い換えができる．
したがって，以下のような実装例で正解を得ることができる．
"""
# 実装例1
N = int(input())
if N < 1000:
    print(N)
if 1000 <= N <= 9999:
    print(N - N % 10)
if 10000 <= N <= 99999:
    print(N - N % 100)
if 100000 <= N <= 999999:
    print(N - N % 1000)
if 1000000 <= N <= 9999999:
    print(N - N % 10000)
if 10000000 <= N <= 99999999:
    print(N - N % 100000)
if 100000000 <= N <= 999999999:
    print(N - N % 1000000)

# 実装例2
def ten(N: int) -> int:
    if N:
        return 10 * ten(N - 1)
    else:
        return 1

N = int(input())
if N < 1000:
    print(N)
for i in range(1, 7):
    if ten(i + 2) <= N < ten(i + 3):
        print(N - N % ten(i))

# 実装例3
S = input()
if len(S) <= 3:
    print(S)
else:
    print(S[:3] + '0' * (len(S) - 3))