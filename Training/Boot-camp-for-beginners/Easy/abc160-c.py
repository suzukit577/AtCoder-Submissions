K, N = map(int, input().split())
A = list(map(int, input().split()))
dist_list = [A[i + 1] - A[i] for i in range(N - 1)]
dist_list.append(A[0] - A[-1] + K)
print(K - max(dist_list))

# 別解
K, N = map(int, input().split())
A = list(map(int, input().split()))
ans = A[-1] - A[0]
for i in range(N):
    i_to_start = K - A[i]
    start_to_i1 = A[i - 1]
    ans = min(ans, i_to_start + start_to_i1)
print(ans)