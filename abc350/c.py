# # K = 0; ans = []

# # def merge(arr, l, m, r):
# #     global K
# #     global ans
    
# #     n1 = m - l + 1
# #     n2 = r - m

# #     L = [arr[l + i] for i in range(n1)]
# #     R = [arr[m + 1 + i] for i in range(n2)]

# #     i = j = 0
# #     k = l

# #     while i < n1 and j < n2:
# #         if L[i] <= R[j]:
# #             arr[k] = L[i]
# #             i += 1
# #         else:
# #             K += 1
# #             ans.append([i + 1,j + n1 + 1])
# #             arr[k] = R[j]
# #             j += 1
# #         k += 1

# #     while i < n1:
# #         arr[k] = L[i]
# #         i += 1
# #         k += 1

# #     while j < n2:
# #         arr[k] = R[j]
# #         j += 1
# #         k += 1

# # def merge_sort(arr, l, r):
# #     global K
# #     global ans
# #     if l < r:
# #         m = (l + r) // 2
# #         merge_sort(arr, l, m)
# #         merge_sort(arr, m + 1, r)
# #         merge(arr, l, m, r)

# # N = int(input())
# # A = list(map(int, input().split()))
# # merge_sort(A, 0, N - 1)
# # print(K)
# # if K != 0:
# #     for a in ans:
# #         print(*a)
        


# # def solve(N, A):
    
# #     return operations

# # N = int(input())
# # A = list(map(int, input().split()))
# # operations = []
# # for i in range(N):
# #     if A[i] != i + 1:
# #         j = A.index(i + 1)
# #         A[i], A[j] = A[j], A[i]
# #         operations.append((i + 1, j + 1))
# # print(len(operations))
# # for op in operations:
# #     print(*op)

# N = int(input())
# A = list(map(int, input().split()))
# count = 0
# count_flag = []
# n = 0
# operations = []

# def merge_sort(A, left, right):
#     global count
#     global count_flag
#     global n
#     global operations
    
#     if left == right:
#         return A

#     mid = (left + right) // 2
#     left_sorted = merge_sort(A, left, mid)
#     right_sorted = merge_sort(A, mid + 1, right)

#     B = []
#     i = 0
#     j = 0
#     while i < len(left_sorted) and j < len(right_sorted):
#         if left_sorted[i] <= right_sorted[j]:
#             count_flag.append(0)
#             B.append(left_sorted[i])
#             if count_flag[n  - 1] != count_flag[n]:
#                 count += 1
#                 operations.append([])
#             i += 1
#         else:
#             count_flag.append(1)
#             B.append(right_sorted[j])
#             j += 1
#         n += 1

#     B.extend(left_sorted[i:])
#     B.extend(right_sorted[j:])
#     return B

# sorted_A = merge_sort(A, 0, N - 1)
# print(count)
# if count > 0:
#     for i in range(count):
#         print(*operations[i])

# 解説(evima)
N = int(input())
A = [0] + list(map(int, input().split()))
pos = [0] * (N + 1)
for i in range(1, N + 1):
    pos[A[i]] = i

ans = []
for i in range(1, N + 1):
    if A[i] != i:
        j = pos[i]
        ans.append(min(i, j), max(i, j))
        A[i], A[j] = A[j], A[i]
        pos[A[i]] = j
        pos[A[j]] = i

print(len(ans))
for a in ans:
    print(*a)