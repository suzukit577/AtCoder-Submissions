S = input()
num_lower, num_upper = 0, 0
for s in S:
    if ord("a") <= ord(s) <= ord("z"):
        num_lower += 1
    else:
        num_upper += 1
print(S.upper() if num_lower < num_upper else S.lower())

# evima 解説
S = input()
u = sum(c.isupper() for c in S)
l = sum(c.islower() for c in S)
if u > l:
    print(S.upper())
else:
    print(S.lower())
