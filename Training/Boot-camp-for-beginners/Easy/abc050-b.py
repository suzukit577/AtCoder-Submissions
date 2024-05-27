N = int(input())
T = list(map(int, input().split()))
M = int(input())
ans = [sum(T) for _ in range(M)]
for i in range(M):
    P, X = map(int, input().split())
    ans[i] += X - T[P - 1]
for a in ans:
    print(a)
