N = int(input())
Lucas = [0] * 87
Lucas[0], Lucas[1] = 2, 1
for i in range(2, 87):
    Lucas[i] = Lucas[i - 1] + Lucas[i - 2]
print(Lucas[N])
