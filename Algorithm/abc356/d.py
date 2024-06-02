# evima 解説
N, M = map(int, input().split())
L, MOD = 60, 998244353

ans = 0
for i in range(L):
    if (M >> i) & 1:
        cycle, rest = (N + 1) // (2 << i), (N + 1) % (2 << i)
        ans += (cycle << i) + max(0, rest - (1 << i))
print(ans % MOD)
