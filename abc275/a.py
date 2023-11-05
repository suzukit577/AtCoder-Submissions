n = int(input())
h = list(map(int,input().split()))
ans = 0
for i in range(1, len(h)):
    if (h[ans] < h[i]):
        ans = i + 1
print(ans)