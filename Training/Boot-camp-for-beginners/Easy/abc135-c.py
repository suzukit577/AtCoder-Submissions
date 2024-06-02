N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
num_init = sum(A)
for i in range(N):
    if A[i] < B[i]:
        A[i + 1] = max(0, A[i + 1] - (B[i] - A[i]))
        A[i] = 0
    else:
        A[i] -= B[i]
print(num_init - sum(A))
