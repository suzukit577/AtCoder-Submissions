from itertools import product

N, K = map(int, input().split())
R = list(map(int, input().split()))
perm_list = list(product(*[range(1, r + 1) for r in R]))
filtered_perm_list = [perm for perm in perm_list if sum(perm) % K == 0]
filtered_perm_list.sort()
for perm in filtered_perm_list:
    print(" ".join(map(str, perm)))


# evima 解説
def f(i: int, A: list[int]) -> str:
    if i == N:
        if sum(A) % K == 0:
            print(" ".join(map(str, A)))
    else:
        for j in range(1, R[i] + 1):
            A.append(j)
            f(i + 1, A)
            A.pop()


N, K = map(int, input().split())
R = list(map(int, input().split()))
f(0, [])
