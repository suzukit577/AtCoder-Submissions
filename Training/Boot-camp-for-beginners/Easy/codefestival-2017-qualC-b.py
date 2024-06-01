# A[i] +- 1 でbit全探索
N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(3**N):
    B = []
    x = i
    for j in range(N):
        if x % 3 == 0:
            B.append(A[j])
        if x % 3 == 1:
            B.append(A[j] - 1)
        if x % 3 == 2:
            B.append(A[j] + 1)
        x //= 3
    for b in B:
        if b % 2 == 0:
            ans += 1
            break
print(ans)

# 公式解説 (余事象を考える)
N = int(input())
A = list(map(int, input().split()))
num_even = 0
for i in range(N):
    if A[i] % 2 == 0:
        num_even += 1
print((3**N) - (2**num_even))
