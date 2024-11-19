a, b = map(int, input().split())
ans = 0
while a != b:
    n = 0
    if a % b == 0:
        n = a // b - 1
        a -= n * b
    elif b % a == 0:
        n = b // a - 1
        b -= n * a
    elif a > b and a != 1 and b != 1:
        n = a // b
        a -= n * b
    elif a < b and a != 1 and b != 1:
        n = b // a
        b -= n * a
    elif a == 1:
        n = b - 1
        b = 1
    elif b == 1:
        n = a - 1
        a = 1
    ans += n
print(ans)

# 解説
a, b = map(int, input().split())
ans = 0
if a < b:
    a, b = b, a
while b > 0:
    ans += a // b
    a %= b
    a, b = b, a
print(ans - 1)

# 解説 (https://qiita.com/Waaaa1471/items/7020575774add4cdeb7e)
a, b = map(int, input().split())
ans = 0
while a != b:
    # b の方が大きい状態を維持
    if a > b:
        a, b = b, a
    # b が a の倍数なら b - a を b//a - 1 回繰り返して終了
    if b % a == 0:
        ans += b//a - 1
        b = a
    # そうでないなら, b - a を b//a 回繰り返す
    else:
        ans += b // a
        b = b % a
print(ans)