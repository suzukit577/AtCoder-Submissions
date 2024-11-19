# evima 解説
N = int(input())
A = list(map(int, input().split()))

x = 0
for a in A:
    c, i = 0, 2
    while i * i <= a:
        while a % i == 0:
            a //= i
            c += 1
        i += 1
    c += 1 if a > 1 else 0
    x ^= c
print("Anna" if x != 0 else "Bruno")
