N = int(input())
A = list(map(int, input().split()))
cnt = 0
nums = [0]
for i in range(N):
    if A[i] == nums[-1] + 1:
        cnt += 1
        nums.append(A[i])
print(-1 if cnt == 0 else N - cnt)
