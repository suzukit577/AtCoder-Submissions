# from bisect import bisect_right

# N, M = map(int, input().split())
# A = sorted(list(map(int, input().split())))
# B = sorted(list(map(int, input().split())))
# j = bisect_right(A, B[0])
# if j == N:
#     ans = -1
# else:
#     ans = A[j]
#     j += 1
#     for i in range(1, M):
#         while j < N and A[j] < B[i]:
#             j += 1
#         if j == N:
#             ans = -1
#             break
#         ans += A[j]
# print(ans)

from bisect import bisect_left

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
ans = 0
j = 0
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
