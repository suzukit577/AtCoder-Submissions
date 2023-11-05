# original
N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
PQ = A[P-1:Q]
RS = A[R-1:S]
if P == 1:
    B = RS + A[Q:R-1] + PQ + A[S:]
else:
    B = A[:P-1] + RS + A[Q:R-1] + PQ + A[S:]
print(*B)

# ans-1
n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))
for i in range(p, q+1):
    a[i-1], a[r-p+i-1] = a[r-p+i-1], a[i-1]
print(*a)

# ans-2
n, p, q, r, s = map(int, input().split())
a = list(map(int, input().split()))
a[p-1:q], a[r-1:s] = a[r-1:s], a[p-1:q]
print(*a)