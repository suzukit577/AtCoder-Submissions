N, M, X = map(int, input().split())
A = list(map(int, input().split()))
l_cost, r_cost = 0, 0
for i in range(M):
    if A[i] < X:
        l_cost += 1
    else:
        r_cost += 1
print(min(l_cost, r_cost))
