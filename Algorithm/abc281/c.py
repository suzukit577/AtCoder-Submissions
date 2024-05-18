n,t = map(int, input().split())
a = list(map(int, input().split()))
rem = t % sum(a)
sum = 0
for i in range(n):
    if (sum + a[i] > rem):
        print(i+1, rem - sum)
        break
    sum += a[i]