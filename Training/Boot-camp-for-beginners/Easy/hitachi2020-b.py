A, B, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = min(A) + min(B)
for _ in range(M):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    if A[x] + B[y] - c <= ans:
        ans = A[x] + B[y] - c
print(ans)
