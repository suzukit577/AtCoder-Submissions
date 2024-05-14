N = int(input())
K = int(input())
X = list(map(int, input().split()))
ans = 0
for x in X:
    ans += 2 * min(abs(x), abs(x - K))
print(ans)