N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))
XA = sorted(zip(X, A))

num_empty = []
for i in range(M):
    left = XA[i][0]
    right = XA[i + 1][0] if i + 1 < M else N + 1
    num_empty.append(right - left - 1)

ans = 0
for i in range(M):
    x, a = XA[i]
    required_empty = a - 1
    available_empty = num_empty[i]
    if available_empty < required_empty:
        print(-1)
        exit()
    ans += (required_empty * (required_empty + 1)) // 2
print(ans)
