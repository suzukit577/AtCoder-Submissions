# 参照: https://qiita.com/zawawahoge/items/8bbd4c2319e7f7746266
def popcount(x: int) -> int:
    """xの立っているビット数をカウントする関数
    (xは64bit整数)"""

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0F0F0F0F0F0F0F0F  # 8bitごと
    x = x + (x >> 8)  # 16bitごと
    x = x + (x >> 16)  # 32bitごと
    x = x + (x >> 32)  # 64bitごと = 全部の合計
    return x & 0x0000007F


N, M = map(int, input().split())
MOD = 998244353
memo = dict()
ans = 0
for i in range(N):
    key = i & M
    if key not in memo.keys():
        memo[key] = popcount(key)
    ans += memo[key]
    ans %= MOD
print(ans)
