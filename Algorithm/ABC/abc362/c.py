N = int(input())
L, R = list(), list()
for _ in range(N):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
if sum(L) * sum(R) > 0:
    print("No")
    exit()
else:
    abs_residue = abs(sum(L))
    for i in range(N):
        diff = min(abs_residue, R[i] - L[i])
        L[i] += diff
        abs_residue -= diff
        if abs_residue == 0:
            break
print("Yes")
print(*L)

# 公式解説
N = int(input())
L, R = [0] * N, [0] * N
for i in range(N):
    L[i], R[i] = map(int, input().split())
if sum(L) > 0 or sum(R) < 0:
    print("No")
    exit()
X = L.copy()
sumX = sum(X)
for i in range(N):
    d = min(R[i] - L[i], -sumX)
    sumX += d
    X[i] += d
print("Yes")
print(*X)
