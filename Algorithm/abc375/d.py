S = input()
left_cnt, right_cnt = [0] * 26, [0] * 26
for s in S:
    right_cnt[ord(s) - ord("A")] += 1
ans = 0
for s in S:
    right_cnt[ord(s) - ord("A")] -= 1
    for c in range(26):
        ans += left_cnt[c] * right_cnt[c]
    left_cnt[ord(s) - ord("A")] += 1
print(ans)


# 公式解説 - 1 (j に注目)
"""
j を固定したとき、条件を満たす (i, k) の個数は
S[i] == S[k] であって、1 <= i < j かつ
j < k <= N を満たす組の個数となる
"""
S = input()
N = len(S)
cum_cnt = [[0] * 26 for _ in range(N + 1)]
for i in range(N):
    for j in range(26):
        cum_cnt[i + 1][j] = cum_cnt[i][j]
    cum_cnt[i + 1][ord(S[i]) - ord("A")] += 1
ans = 0
for i in range(1, N - 1):
    for j in range(26):
        l, r = cum_cnt[i][j], cum_cnt[N][j] - cum_cnt[i + 1][j]
        ans += l * r
print(ans)


# 公式解説 - 2 (i, k に注目)
"""
S[i] == S[k] のとき、j は i < j < k を満たすものであれば
すべて条件を満たすので、j は (k - i - 1 ) 通りの選び方ががある
"""
S = input()
N = len(S)
cnt, cum_sum = [0] * 26, [0] * 26
ans = 0
for i in range(N):
    c = ord(S[i]) - ord("A")
    # cnt[c] 個の距離 (i - 1) それぞれから、過去に文字 S[i] が出現したインデックスを引く
    ans += (i - 1) * cnt[c] - cum_sum[c]
    cnt[c] += 1
    cum_sum[c] += i
print(ans)
