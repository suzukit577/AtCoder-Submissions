def shift_char(S: str):
    S = chr(ord(S[0]) + 1) + chr(ord(S[1]) + 1)
    if ord(S[0]) - ord('E') > 0:
        S = chr(ord(S[0]) - 5) + S[1]
    if ord(S[1]) - ord('E') > 0:
        S = S[0] + chr(ord(S[1])  -  5)
    return S

S = input()
T = input()
for i in range(5):
    S = shift_char(S)
    if S == T  or ''.join(list(reversed(S))) == T:
        print('Yes')
        exit()
print('No')