def modular_remainder(N: int, M: int) -> int:
    num_digits_N = len(str(N))
    power_mod = pow(10, num_digits_N * N, M)
    base_mod = pow(10, num_digits_N, M)
    num_mod = (power_mod - 1) % M
    inv_mod = pow(base_mod - 1, -1, M)
    N_mod = N % M
    remainder = (N_mod * num_mod * inv_mod) % M
    return remainder


N = int(input())
MOD = 998244353
print(modular_remainder(N, MOD))


# evima 解説 (Python)
# pow 関数を用いずに自力実装するなら "繰り返し二乗法", "乗法の逆元", "フェルマーの小定理"
N = int(input())
MOD = 998244353
common_ratio = pow(10, len(str(N)), MOD)  # 公比
print(N * (1 - pow(common_ratio, N, MOD)) * pow(1 - common_ratio, -1, MOD) % MOD)


# 公式解説
def extended_Euclidean(a: int, b: int) -> tuple[int, int, int]:
    """
    拡張ユークリッドの互除法: O(log(min(a, b)))

    入力
    a: int, b: int
    -> 互いに素な 2 整数 a, b に対して, 二元一次方程式 ax + by = gcd(a, b) の係数 a, b

    出力
    二元一次不定方程式 ax + by = gcd(a, b) について,
    gcd(a, b) および方程式の解 x, y からなる 3 つ組 (gcd(a, b), x, y)
    """
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_Euclidean(b % a, a)
        return gcd, y - (b // a) * x, x


def mod_inverse_via_extended_Euclidean(a: int, mod: int) -> int:
    """
    拡張ユークリッドの互除法による乗法逆元の計算: O(log(min(a, mod)))
    逆元存在条件: a と mod が互いに素, すなわち, gcd(a, mod) = 1

    入力
    a: int, mod: int
    -> 互いに素な 2 整数 a, mod (a は負の整数でもよい)

    出力
    mod を法とした下での a の乗法逆元 x,
    すなわち, ax ≡ 1 (mod mod) を満たす整数 x であって, 0 <= x < mod を満たすもの

    参考: https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a#3-3-%E9%80%86%E5%85%83%E3%81%AE%E6%B1%82%E3%82%81%E6%96%B9%E3%81%AE%E6%A6%82%E8%A6%81
    """
    a %= mod  # 負の数を正の数に変換
    gcd, x, _ = extended_Euclidean(a, mod)
    if gcd != 1:
        raise ValueError(f"No modular inverse exists for {a} and {mod}")
    else:
        return x % mod


N = int(input())
K = len(str(N))
MOD = 998244353
common_ratio = pow(10, K, MOD)  # 公比
mod_inv = mod_inverse_via_extended_Euclidean(1 - common_ratio, MOD)
ans = ((N % MOD) * ((1 - pow(common_ratio, N, MOD)) % MOD) * mod_inv) % MOD
print(ans)


# ユーザ解説
P = 998244353
N = int(input())


def f(N: int, i: int) -> int:
    if i == 1:
        return N % P
    K = len(str(N))
    if i % 2 == 0:
        t = f(N, i // 2)
        return (t * pow(10, i // 2 * K, P) + t) % P
    else:
        return (f(N, i - 1) * 10**K + N) % P


print(f(N, N))
