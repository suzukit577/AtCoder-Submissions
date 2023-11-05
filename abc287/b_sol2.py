N, M = map(int, input().split())
S = [int(input()) for _ in range(N)]
exist = [False for _ in range(1000)]
for _ in range(M):
    t = int(input())
    exist[t] = True
ans = 0
for i in range(N):
    if exist[S[i] % 1000]:
        ans += 1
print(ans)