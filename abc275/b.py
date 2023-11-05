a, b, c, d, e, f = map(int, input().split())
n = 998244353
ans = ((a * b * c - d * e * f) % n)
print(ans)