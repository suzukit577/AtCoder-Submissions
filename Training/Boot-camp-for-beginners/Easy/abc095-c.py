A, B, C, X, Y = map(int, input().split())
if A + B > 2 * C:
    print(
        min(
            2 * C * max(X, Y), 2 * C * min(X, Y) + A * max(X - Y, 0) + B * max(Y - X, 0)
        )
    )
else:
    print(A * X + B * Y)

# ユーザ解説
A, B, C, X, Y = map(int, input().split())
ans = 10**9
for ab in range(0, 201010):
    sm = C * ab
    x = X - ab // 2
    y = Y - ab // 2
    if x > 0:
        sm += x * A
    if y > 0:
        sm += y * B
    ans = min(ans, sm)
print(ans)
