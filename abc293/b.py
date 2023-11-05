n = int(input())
a = list(map(int, input().split()))
called = [False for _ in range(n)]
for i in range(n):
    if not called[i]:
        called[a[i]-1] = True
ans = []
for i in range(n):
    if not called[i]:
        ans.append(i+1)
print(len(ans))
print(*ans)