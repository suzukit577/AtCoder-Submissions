N, K, Q = map(int, input().split())
correct = [0] * N
points = [K] * N
for _ in range(Q):
    A = int(input())
    correct[A - 1] += 1
for i in range(N):
    points[i] -= Q - correct[i]
    print("Yes" if points[i] > 0 else "No")

# 公式解説
N, K, Q = map(int, input().split())
points = [K - Q] * N
for _ in range(Q):
    A = int(input())
    points[A - 1] += 1
for i in range(N):
    print("Yes" if points[i] > 0 else "No")
