S = list(map(int, input().split()))
c1 = True; c2 = True; c3 = True
for i in range(1, len(S)):
    if S[i] < S[i - 1]:
        c1 = False
for s in S:
    if s < 100 or 675 < s:
        c2 = False
    if s % 25 != 0:
        c3 = False
print('Yes' if c1 and c2 and c3 else 'No')

# 公式解説
s = list(map(int, input().split()))
for i in range(8):
    if i < 7 and s[i] > s[i + 1]:
        print('No')
        exit()
    if s[i] < 100 or s[i] > 675 or s[i] % 25 != 0:
        print('No')
        exit()
print('Yes')