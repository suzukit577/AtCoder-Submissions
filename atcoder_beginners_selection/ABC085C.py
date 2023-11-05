import sys

n, y = map(int, input().split())

for i in range(n+1):
    for j in range(n-i+1):
        k = n - i - j
        if k >= 0:
            if (10000 * i + 5000 * j + 1000 * k == y):
                print(i,j,k)
                sys.exit()

print(-1,-1,-1)