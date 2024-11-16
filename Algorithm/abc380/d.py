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
