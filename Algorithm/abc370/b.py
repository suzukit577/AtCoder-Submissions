N = int(input())
A = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]
current = 0
for i in range(N):
    if current >= i:
        current = A[current][i]
    else:
        current = A[i][current]
print(current + 1)

# evima 解説
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
x = 1
for i in range(1, N + 1):
    if x >= i:
        x = A[x - 1][i - 1]
    else:
        x = A[i - 1][x - 1]
print(x)
