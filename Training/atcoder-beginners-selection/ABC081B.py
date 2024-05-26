n = int(input())
a = list(map(int, input().split()))
cnt = 0
while all(x % 2 == 0 for x in a):
    for i in range(n):
        a[i] /= 2
    cnt += 1
print(cnt)