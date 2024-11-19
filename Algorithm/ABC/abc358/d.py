N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
ans, j = 0, 0
for b in B:
    while j < N and A[j] < b:
        j += 1
    if j == N:
        print(-1)
        break
    ans += A[j]
    j += 1
else:
    print(ans)


# evima 解説 (平衡二分探索木)
from sortedcontainers import SortedList

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s = SortedList(A)
ans = 0
for b in B:
    i = s.bisect_left(b)
    if i == len(s):
        ans = -1
        break
    ans += s[i]
    s.pop(i)
print(ans)
