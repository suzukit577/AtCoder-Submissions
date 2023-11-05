n = int(input())
a = list(map(int, input().split()))
ans = []
for i in range(n):
    if a[i] % 2 == 0:
        ans.append(a[i])
print(*ans)