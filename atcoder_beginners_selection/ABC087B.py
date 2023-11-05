a, b, c, x = [int(input()) for i in range(4)]
cnt = 0

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            sum = 500 * i + 100 * j + 50 * k
            if sum == x:
                cnt += 1

print(cnt)