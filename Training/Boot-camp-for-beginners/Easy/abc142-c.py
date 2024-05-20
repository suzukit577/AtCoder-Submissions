N = int(input())
A = list(map(int, input().split()))
ordered_students = [[A[i], i + 1] for i in range(N)]
ordered_students.sort(key=lambda x: x[0])
for i in range(N):
    print(ordered_students[i][1], end=" ")

# 公式解説
N = int(input())
A = list(map(int, input().split()))
rev = [0] * N
for i in range(N):
    rev[A[i] - 1] = i + 1
for i in range(N):
    print(rev[i], end=" ")