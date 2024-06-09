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


# 自力実装
