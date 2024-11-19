N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(2, 2 * N):
    if A[i - 2] == A[i]:
        ans += 1
print(ans)

# evima 解説
N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(len(A) - 2):
    ans += A[i] == A[i + 2]
print(ans)
