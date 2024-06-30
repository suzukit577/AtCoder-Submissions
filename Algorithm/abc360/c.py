from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))
dd = defaultdict(list)
for i in range(N):
    dd[A[i]].append(W[i])
ans = 0
for k, v in dd.items():
    if len(v) > 1:
        num_item = len(v)
        ans += sum(sorted(v)[: num_item - 1])
print(ans)

# evima 解説
N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))
b = [0] * (N + 1)
for i in range(N):
    b[A[i]] = max(b[A[i]], W[i])
print(sum(W) - sum(b))
