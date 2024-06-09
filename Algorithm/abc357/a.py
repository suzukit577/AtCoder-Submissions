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

# evima 解説
N, M = map(int, input().split())
H = list(map(int, input().split()))
ans = N
for i in range(N):
    if H[i] > M:
        ans = i
        break
    M -= H[i]
print(ans)
