N = int(input())
counts = [0] * (N + 1)
for i in range(1, N + 1):
    j = i
    while j % 2 == 0 and j != 0:
        j //= 2
        counts[i] += 1
if sum(counts) == 0:
    print(1)
else:
    print(counts.index(max(counts)))

# 解説
N = int(input())
num_list = [2 ** i for i in range(7)]
for num in num_list[::-1]:
    if num <= N:
        print(num)
        exit()