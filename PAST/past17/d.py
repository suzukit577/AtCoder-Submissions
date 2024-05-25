A, B, C = map(int, input().split())
X = list(map(int, input().split()))
free = 0
general = B
premium = C
for x in X:
    free += A * max(x - 3, 0)
    general += A * max(x - 50, 0)
print(min(free, general, premium))
