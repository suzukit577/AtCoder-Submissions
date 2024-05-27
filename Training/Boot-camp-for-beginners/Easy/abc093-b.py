A, B, K = map(int, input().split())
small, large = list(), list()
if K >= (B - A) // 2 + 1:
    ans = [i for i in range(A, B + 1)]
else:
    for i in range(K):
        small.append(A + i)
        large.append(B - i)
    ans = sorted(set(small + large[::-1]))
for a in ans:
    print(a)
