N = int(input())
S = input()
T = input()
flag = True
for i in range(N):
    if S[i] != T[i] and {S[i], T[i]} != {'1', 'l'} and {S[i], T[i]} != {'0', 'o'}:
        flag = False
print('Yes' if flag else 'No')


# 公式解説
def is_sim_char(c, d):
    return (
        c == d
        or (c == '0' and d == 'o')
        or (c == 'o' and d == '0')
        or (c == 'l' and d == '1')
        or (c == '1' and d == 'l')
    )

def is_sim_string(s, t):
    for i in range(len(s)):
        if not is_sim_char(s[i], t[i]):
            return False
    return True

N = int(input())
S = input()
T = input()
print('Yes' if is_sim_string(S, T) else 'No')


# ユーザー解説
N = int(input())
S = input().replace('0', 'o').replace('1', 'l')
T = input().replace('0', 'o').replace('1', 'l')
print('Yes' if S == T else 'No')