def f(n: int) -> int:
    return n // 2 if n % 2 == 0 else 3 * n + 1


s = int(input())
a = s
A = set([a])
for i in range(2, 1000001):
    next_a = f(a)
    if next_a in A:
        print(i)
        exit()
    A.add(next_a)
    a = next_a
