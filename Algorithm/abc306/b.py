A = list(map(int, input().split()))
ans = 0
for i in range(len(A)):
    ans += A[i] * (2 ** i)
print(ans)

# 公式解説
A = list(map(int, input().split()))
ans = 0
for i in range(64):
    ans += A[i] << i
print(ans)

# 別解
A = input().split()
print(int(''.join(reversed(A)), 2))