A, B = map(int, input().split())
if A == 3 or A == 6:
    print('No')
else:
    if B == A + 1:
        print('Yes')
    else:
        print('No')

# 公式解説
A, B = map(int, input().split())
print('Yes' if A % 3 != 0 and A + 1 == B else 'No')

# 別解
# A, B が書かれたマスがそれぞれ上から何行目, 左から何列目にあるか求める
# A - 1 を 3 で割った際の商と余りが，A が書かれた行と列にそれぞれ対応
A, B = map(int, input().split())
ra, ca = (A - 1) // 3, (A - 1) % 3
rb, cb = (B - 1) // 3, (B - 1) % 3
print('Yes' if ra == rb and ca + 1 == cb else 'No')