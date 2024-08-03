N = int(input())
A = list(map(int, input().split()))
SA = sorted(A)
for i in range(N):
    if A[i] == SA[-2]:
        print(i + 1)
        break
