S = input()
T = input()
cnt_S_at = S.count('@')
cnt_T_at = T.count('@')
alphabets = 'abcdefghijklmnopqrstuvwxyz'
reps = 'atcoder'
for alphabet in alphabets:
    cnt_S = S.count(alphabet)
    cnt_T = T.count(alphabet)
    if cnt_S > cnt_T:
        if alphabet in reps and cnt_T_at > 0 and cnt_S - cnt_T <= cnt_T_at:
            cnt_T_at -= 1
        else:
            print('No')
            exit()
    elif cnt_T > cnt_S:
        if alphabet in reps and cnt_S_at > 0 and cnt_T - cnt_S <= cnt_S_at:
            cnt_S_at -= 1
        else:
            print('No')
            exit()
print('Yes')

# 公式解説
from collections import defaultdict

S = input()
T = input()
Scnt = defaultdict(int)
Tcnt = defaultdict(int)
for c in S: Scnt[c] += 1
for c in T: Tcnt[c] += 1

for c in 'atcoder':
    M = max(Scnt[c], Tcnt[c])
    if Scnt['@'] < M - Scnt[c] or Tcnt['@'] < M - Tcnt[c]:
        print('No')
        exit()
    Scnt['@'] -= M - Scnt[c]
    Scnt[c] = M
    Tcnt['@'] -= M - Tcnt[c]
    Tcnt[c] = M

print('Yes' if Scnt == Tcnt else 'No')

# ユーザー解説 (最大二部マッチング問題に帰着)