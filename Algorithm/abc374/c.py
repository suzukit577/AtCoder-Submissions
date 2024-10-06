N = int(input())
K = sorted(list(map(int, input().split())))
ans, diff = 0, 10**10
for mask in range(1 << N):
    A, B = 0, 0
    for i in range(N):
        if mask & (1 << i):
            A += K[i]
        else:
            B += K[i]
    diff_new = abs(A - B)
    if diff_new < diff:
        diff = diff_new
        ans = max(A, B)
print(ans)
