N, M = map(int, input().split())
K, A = [0] * N, [[] * N for _ in range(N)]
foods = set()
for i in range(N):
    input_list = list(map(int, input().split()))
    K[i], A[i] = input_list[0], set(input_list[1:])
    foods |= A[i]

for i in range(N):
    foods &= A[i]
print(len(foods))

# 公式解説
N, M = map(int, input().split())
cnt = [0] * M
for i in range(N):
    input_list = list(map(int, input().split()))
    K, A = input_list[0], input_list[1:]
    for j in range(K):
        cnt[A[j] - 1] += 1
ans = 0
for i in range(M):
    if cnt[i] == N:
        ans += 1
print(ans)

# ユーザ解説
N, M = map(int, input().split())
A = [[0] * 31 for _ in range(31)]
for i in range(N):
    input_list = list(map(int, input().split()))
    K, AA = input_list[0], input_list[1:]
    for j in range(K):
        A[i][AA[j] - 1] = 1

ans = 0
for i in range(M):
    cnt = 0
    for j in range(N):
        if A[j][i] > 0:
            cnt += 1
    if cnt == N:
        ans += 1
print(ans)
