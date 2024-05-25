N, A, B = map(int, input().split())
ans = 0
for i in range(N + 1):
    digit_sum = sum(list(map(int, list(str(i)))))
    if A <= digit_sum <= B:
        ans += i
print(ans)

# 公式解説
N, A, B = map(int, input().split())
ans = 0
for i in range(N + 1):
    c, t = 0, i
    for j in range(5):
        c += t % 10
        t //= 10
    if A <= c <= B:
        ans += i
print(ans)
