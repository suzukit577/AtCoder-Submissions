import math

X = int(input())
ans = 10**8
for i in range(X, 10**6):
    for j in range(2, math.ceil(math.sqrt(i))):
        if i % j == 0:
            break
    else:
        ans = i
        break
print(ans)
