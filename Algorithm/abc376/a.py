N, C = map(int, input().split())
T = list(map(int, input().split()))
ans, time = 0, 0
for i in range(N):
    if i == 0:
        ans += 1
        time = T[i]
    else:
        if T[i] - time >= C:
            ans += 1
            time = T[i]
print(ans)


# 公式解説
N, C = map(int, input().split())
T = list(map(int, input().split()))
ans, pre = 1, T[0]
for i in range(1, N):
    if T[i] - pre >= C:
        ans += 1
        pre = T[i]
print(ans)
