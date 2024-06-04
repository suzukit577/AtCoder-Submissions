# evima 解説
N, M = map(int, input().split())
L, MOD = 60, 998244353

ans = 0
for i in range(L):
    if M & (1 << i):  # M の i-bit 目が立っているとき
        cycle, rest = (N + 1) // (2 << i), (N + 1) % (2 << i)
        ans += (cycle << i) + max(0, rest - (1 << i))
print(ans % MOD)


# 公式解説
def count_numbers_with_i_th_bit_set(i: int, n: int) -> int:
    """
    0 以上 n 以下の整数のうち i-bit 目が 1 であるものの個数を求める関数
    時間計算量: O(log n)

    入力:
    i: 何番目の bit が 1 であるかを示す (0-indexed)
    n: 整数

    出力:
    0 以上 n 以下の整数のうち i-bit 目が 1 であるものの個数

    次の2つの性質を用いる:

    [性質1]
    k を非負整数とすると, 0 以上 k * (2 ** (i + 1)) 未満の整数のうち，
    i-bit 目が 1 であるものは k * (2 ** i) 個ある
    > すべての非負整数 j について j の i-bit 目と j + 2 ** (i + 1) の i-bit 目は一致する
    > 0 以上 2 ** (i + 1) 未満の整数のうち i-bit 目が 1 であるものはちょうど 2 ** i 個ある

    [性質2]
    k を非負整数, l を 2 ** (i + 1) 未満の整数とすると，
    k * (2 ** (i + 1)) 以上 k * (2 ** (i + 1)) + l 以下の整数のうち，
    i-bit 目が 1 であるものの個数は次の通り．
    - l が 2 ** i 未満のとき -> 0,
    - l が 2 ** i 以上のとき -> l - (2 ** i) + 1
    """
    bit_value = 2**i
    # n を 2 ** (i + 1) の商と余りに分けて答えを求める
    k, l = n // (2 * bit_value), n % (2 * bit_value)
    count = k * bit_value
    if l >= bit_value:
        count += l - bit_value + 1
    return count


N, M = map(int, input().split())
L, MOD = 60, 998244353
ans = 0
for i in range(L):
    if M & (1 << i):  # M の i-bit 目が立っているとき
        # 0 以上 N 以下の整数のうち，i-bit 目が立っているものの個数を ans に加算する
        """
        k を非負整数とすると，0 以上 k * (2 ** (i + 1)) 未満の整数のうち，
        i-bit 目が立っているものは k * (2 ** i) 個ある
        """
        ans += count_numbers_with_i_th_bit_set(i, N)
        ans %= MOD
print(ans)
