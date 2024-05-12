N = int(input())
H = list(map(int, input().split()))
ans = -1
for i in range(N):
    if H[i] > H[0]:
        ans = i + 1
        break
print(ans)