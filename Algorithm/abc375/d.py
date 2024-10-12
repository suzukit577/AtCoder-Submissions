S = input()
right_cnt = [0] * 26
for s in S:
    right_cnt[ord(s) - ord("A")] += 1
ans = 0
left_cnt = [0] * 26
for j in range(len(S)):
    right_cnt[ord(S[j]) - ord("A")] -= 1
    for c in range(26):
        ans += left_cnt[c] * right_cnt[c]
    left_cnt[ord(S[j]) - ord("A")] += 1
print(ans)
