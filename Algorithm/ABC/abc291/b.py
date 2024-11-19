n = int(input())
x = sorted(list(map(int, input().split())))
sum = 0
for i in range(n,4*n):
    sum += x[i]
print(sum / (3*n))