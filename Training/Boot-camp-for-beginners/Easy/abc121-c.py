N, M = map(int, input().split())
drinks = []
for _ in range(N):
    A, B = map(int, input().split())
    drinks.append((A, B))
drinks.sort(key=lambda x: x[0])
num_drink, ans = 0, 0
for d in drinks:
    num_buy = min(d[1], M)
    num_drink += num_buy
    ans += num_buy * d[0]
    M -= num_buy
    if M == 0:
        break
print(ans)
