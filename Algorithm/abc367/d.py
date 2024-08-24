# evima 解説
N, M = map(int, input().split())
A = list(map(int, input().split()))
s = sum(A)
A += A

c = [0] * M
d, ans = 0, 0
for i in range(2 * N):
    if i >= N:
        c[(d - s) % M] -= 1
        ans += c[d % M]
    c[d % M] += 1
    d += A[i]
print(ans)
