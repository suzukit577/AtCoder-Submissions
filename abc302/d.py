# 公式解説
N, M, D = map(int, input().split())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))
while True:
    if len(A) == 0 or len(B) == 0:
        print(-1)
        exit()
    s, t = A[-1], B[-1]
    if abs(s - t) <= D:
        print(s + t)
        exit()
    else:
        if s < t:
            del B[-1]
        else:
            del A[-1]

# 別解
import bisect

N, M, D = map(int, input().split())
A = sorted(map(int, input().split()))
B = list(map(int, input().split()))
ans = -1
for b in B:
    i = bisect.bisect_right(A, b + D) - 1
    if i >= 0 and A[i] >= b - D:
        ans = max(ans, A[i] + b)
print(ans)