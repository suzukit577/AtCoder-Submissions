import math

N = int(input())
for x in range(1, N + 1):
    n = math.floor(x * 1.08)
    if n == N:
        print(x)
        exit()
else:
    print(':(')