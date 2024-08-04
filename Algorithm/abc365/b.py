N = int(input())
A = list(map(int, input().split()))
SA = sorted(A)
for i in range(N):
    if A[i] == SA[-2]:
        print(i + 1)
        break

# evima 解説
N = int(input())
A = list(map(int, input().split()))
print(A.index(sorted(A)[-2]) + 1)
