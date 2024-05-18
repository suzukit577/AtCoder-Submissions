N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
points = [C] * N
for i in range(N):
    for j in range(M):
        points[i] += A[i][j] * B[j]
is_correct = [True if points[i] > 0 else False for i in range(N)]
print(sum(is_correct))