N = int(input())
V = list(map(int, input().split()))
for _ in range(N - 1):
    V.sort(reverse=True)
    x, y = V.pop(), V.pop()
    z = (x + y) / 2
    V.append(z)
print(*V)

# ユーザ解説
N = int(input())
V = list(map(int, input().split()))
V.sort()
ans = V[0]
for i in range(1, N):
    ans = (ans + V[i]) / 2
print(ans)