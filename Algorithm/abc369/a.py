A, B = sorted(map(int, input().split()))
if A == B:
    print(1)
elif (A + B) % 2 == 0:
    print(3)
else:
    print(2)

# evima 解説 - 1
A, B = map(int, input().split())
if A == B:
    print(1)
else:
    print(3 if (A + B) % 2 == 0 else 2)

# evima 解説 - 2
A, B = map(int, input().split())
ans = 0
for i in range(-100, 201):
    a, b, c = sorted([A, B, i])
    ans += b - a == c - b
print(ans)
