S = input()
Q = int(input())
K = list(map(int, input().split()))
init_length = len(S)
ans = []
for k in K:
    k -= 1
    length = init_length
    while length <= k:
        length *= 2
    rev_cnt = 0
    while length > init_length:
        half_length = length // 2
        if k >= half_length:
            k -= half_length
            rev_cnt += 1
        length = half_length
    res_char = S[k]
    if rev_cnt % 2 == 1:
        res_char = res_char.swapcase()
    ans.append(res_char)
print(" ".join(ans))


# 公式解説
S = input()
Q = int(input())
K = list(map(lambda x: int(x) - 1, input().split()))
for k in K:
    blk = k // len(S)
    pt = k % len(S)
    if bin(blk).count("1") % 2:
        print(chr(ord(S[pt]) ^ 32), end=" ")
    else:
        print(S[pt], end=" ")


# ユーザー解説 - クエリあたりの演算回数を O(log log w) とする解法 by MMNMM


# ユーザー解説 - 直接的な実装 by evima
S = input()
Q = int(input())
K = map(int, input().split())


def f(k: int, level: int) -> str:
    if level == 0:
        return S[k - 1]
    h = len(S) << (level - 1)
    if k <= h:
        return f(k, level - 1)
    return chr(ord(f(k - h, level - 1)) ^ 32)


for k in K:
    print(f(k, 60), end=" ")
