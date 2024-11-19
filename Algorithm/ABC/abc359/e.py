N = int(input())
H = list(map(int, input().split()))

s = [(0, 0)]
ans = 0
for i in range(N):
    w = 1
    while len(s) and s[-1][0] <= H[i]:
        w += s[-1][1]
        ans -= s[-1][0] * s[-1][1]
        s.pop()
    ans += H[i] * w
    s.append((H[i], w))
    print(ans + 1)
