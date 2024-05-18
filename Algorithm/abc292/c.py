def make_divisors(n):
    """
    - 自然数nの約数を列挙する関数
    - 計算量: O(sqrt(n))
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

n = int(input())
ans = 0
for ab in range(1,n):
    cd = n - ab
    div_ab = make_divisors(ab)
    div_cd = make_divisors(cd)
    ans += len(div_ab) * len(div_cd)
print(ans)