N, M = map(int, input().split())
H = list(map(int, input().split()))
s, ans = 0, 0
for i in range(N):
    s += H[i]
    if s <= M:
        ans += 1
    else:
        break
print(ans)
