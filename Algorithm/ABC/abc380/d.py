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


# ユーザー解説 - クエリあたりの演算回数を O(log log w) とする解法 by MMNMM


# ユーザー解説 - 直接的な実装 by evima
