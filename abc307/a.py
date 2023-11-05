N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(N):
    ans.append(sum(A[7 * i:7 * (i + 1)]))
print(*ans)

# 公式解説
N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    sum = 0
    for j in range(7):
        sum += A[7 * i + j]
    if i != N - 1:
        print(sum, end=' ')
    else:
        print(sum, end='\n')

# 別解
N = int(input())
A = list(map(int, input().split()))
ans = [sum(A[7 * i:7 * i + 7]) for i in range(N)]
print(*ans)