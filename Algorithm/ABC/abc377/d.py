# 公式解説
"""
まず、重要な事実として整数の組 (l, r) が条件を満たすなら (l + 1, r) も条件を満たします。
これにより、以下の条件を満たす d_r が存在します：
- r を固定した際に (l, r) が条件を満たすような l は d_r 以上 r 以下の整数のみである
この d_r が各 r に対して求まれば、求める答えは \sum_{r = 1}^{M} (r - d_r + 1) となります。
以下ではこの d_r を求めることを考えます。

d_r-1 が求まっていると仮定して d_r を求めることを考えます。
もし R_i = r を満たす i が存在しない場合、新しく制約は増えないので d_r = d_r-1 となります。
そのような i が存在する場合、R_i = r を満たす i に対する L_i の最大値を L_max とすると
d_r = max(d_r-1, L_max + 1) となります。
この漸化式にしたがって d_1 から順に求めていくことで d_r を求めることができます。

以上を適切に実装することでこの問題を解くことができます。
計算量は O(N + M) となります。
"""
N, M = map(int, input().split())
d = [1 for _ in range(M + 1)]
for _ in range(N):
    L, R = map(int, input().split())
    d[R] = max(d[R], L + 1)
for r in range(1, M + 1):
    d[r] = max(d[r], d[r - 1])
ans = 0
for r in range(1, M + 1):
    ans += r - d[r] + 1
print(ans)
