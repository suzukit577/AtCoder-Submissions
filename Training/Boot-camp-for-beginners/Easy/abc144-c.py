def make_divisors(n):
    """
    - 自然数nの約数を列挙する関数
    - 計算量: O(√n)
    - 入力: n
    - 出力: nの約数を要素に持つlist
    """
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N = int(input())
divisors = make_divisors(N)
M = len(divisors) // 2 + 1
ans = 10**13
for i in range(M):
    ans = min(ans, divisors[i] + divisors[-i - 1] - 2)
print(ans)

# 公式解説
import math

N = int(input())
ans = 10**13
for a in range(1, math.ceil(math.sqrt(N)) + 1):
    if N % a == 0:
        ans = min(ans, a + N // a - 2)
print(ans)
