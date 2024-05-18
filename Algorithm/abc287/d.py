def match_or_not(a: str, b: str) -> bool:
    return a == "?" or b == "?" or a == b

S = list(input())
T = list(input())
pre = [False for _ in range(len(S)+1)]
suf = [False for _ in range(len(S)+1)]

pre[0] = True
for i in range(len(T)):
    if not match_or_not(S[i], T[i]):
        break
    pre[i+1] = True

S.reverse()
T.reverse()

suf[0] = True
for i in range(len(T)):
    if not match_or_not(S[i], T[i]):
        break
    suf[i+1] = True

for i in range(len(T)+1):
    if pre[i] and suf[len(T)-i]:
        print("Yes")
    else:
        print("No")