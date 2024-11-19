S = input()
num = int(S[-3:])
if 1 <= num <= 349 and num != 316:
    print('Yes')
else:
    print('No')

# 解説(evima)
S = input()
n = int(S[3:])
print("Yes" if 1 <= n <= 349 and n != 316 else "No")