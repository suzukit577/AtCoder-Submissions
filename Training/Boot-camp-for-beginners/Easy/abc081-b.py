N = int(input())
A = list(map(int, input().split()))
counts = [0] * N
for i in range(N):
    while A[i] % 2 == 0:
        counts[i] += 1
        A[i] //= 2
print(min(counts))
