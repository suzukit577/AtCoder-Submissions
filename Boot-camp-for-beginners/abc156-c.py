N = int(input())
X = list(map(int, input().split()))
ans = 10 ** 8
for i in range(101):
    sum = 0
    for x in X:
        sum += (x - i) ** 2
    if sum < ans:
        ans = sum
print(ans)