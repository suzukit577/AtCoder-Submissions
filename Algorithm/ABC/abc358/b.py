N, A = map(int, input().split())
T = list(map(int, input().split()))
ans = [0] * N
ans[0] = T[0] + A
for i in range(1, N):
    if T[i] >= ans[i - 1]:
        ans[i] = T[i] + A
    else:
        ans[i] = ans[i - 1] + A
for a in ans:
    print(a)

# evima 解説
N, A = map(int, input().split())
T = list(map(int, input().split()))
pre = 0  # 直前の人の購入完了時刻
for t in T:
    u = max(t, pre) + A
    print(u)
    pre = u
