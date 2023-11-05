# 公式解説
# omitted

# 楽な実装
'''
S の ? をすべて 0 に変えて得られる数が N より大きいなら，答えは -1 です．そうでないなら，いま 0 に変えた各桁に対して，上から順に次を行えば答えが得られます：「その桁を 1 に変えても数が N を超えないなら， 1 に変える」.

'''
S = list(reversed(input()))
N = int(input())
s = 0
for i in range(len(S)):
    s |= (S[i] == '1') << i
if s > N:
    print(-1)
else:
    for i in reversed(range(len(S))):
        if S[i] == '?' and (s | 1 << i) <= N:
            s |= 1 << i
    print(s)