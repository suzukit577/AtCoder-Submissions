N = int(input())
S = [0 for _ in range(N)]
C = [0 for _ in range(N)]
for i in range(N):
    s, c = input().split()
    S[i] = s
    C[i] = int(c)
T = sum(C)
S.sort()
print(S[T % N])