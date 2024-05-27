N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
diff = [0] * N
for i in range(N):
    diff[i] = abs(A - (T - H[i] * 0.006))
print(diff.index(min(diff)) + 1)
