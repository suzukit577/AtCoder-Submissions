import math

a, b = input().split()
num = int(a + b)
ub = math.sqrt(100100)
for i in range(round(ub) + 1):
    if i ** 2 == num:
        print('Yes')
        break
else:
    print('No')