N = int(input())
A = list(map(int, input().split()))
ans, cnt = 0, 0
while cnt < N - 1:
    A.sort(reverse=True)
    A[0] -= 1
    A[1] -= 1
    ans += 1
    if A[0] == 0:
        cnt += 1
    if A[1] == 0:
        cnt += 1
print(ans)


# evima 解説
N = int(input())
A = list(map(int, input().split()))
INF = 10**9

for t in range(INF):
    A.sort(reverse=True)
    if A[1] <= 0:
        print(t)
        break
    A[0] -= 1
    A[1] -= 1
