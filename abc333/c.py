# N = int(input())
# q = N // 3
# r = N % 3
# ans = 3 * int('1' * (q + 1))
# if q != 0 and r == 0:
#     ans -= 10 ** q
# elif r == 2:
#     ans += 10 ** (q + 1)
# print(ans)

# 0   1 1 1 1
#     2 1 1 11

#     3 1 11 11
# 1   4 11 11 11
#     5 11 11 111

#     6 11 111 111
# 2   7 111 111 111
#     8 111 111 1111

#     9 111 1111 1111

# 10 1111 1111 1111

def find_repunit_sum(N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(1, 4):
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i - j] + int('1' * j))
    return dp[N]

N = int(input())
result = find_repunit_sum(N)
print(result)