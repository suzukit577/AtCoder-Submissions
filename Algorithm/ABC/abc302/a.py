A, B = map(int, input().split())
print(A // B if A % B == 0 else A // B + 1)

# 公式解説
A, B = map(int, input().split())
print((A + B - 1) // B)