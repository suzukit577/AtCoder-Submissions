n = int(input())
s = [int(i) for i in input().split()]
a = []

for i in range(n):
    if i == 0:
        a.append(s[i])
    else:
        a.append(s[i] - s[i-1])

for i in range(n):
    print(a[i], end=' ')