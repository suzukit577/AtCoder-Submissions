A, B, C = map(int, input().split())
A, B, C = sorted([A, B, C])
ans = 0 if A % 2 == 0 or B % 2 == 0 or C % 2 == 0 else A * B
print(ans)
