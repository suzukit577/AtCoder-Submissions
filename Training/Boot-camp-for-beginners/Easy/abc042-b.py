N, L = map(int, input().split())
S = list()
for _ in range(N):
    S.append(input())
S.sort()
ans = ""
for s in S:
    ans += s
print(ans)
