N, K = map(int, input().split())
A = list(map(int, input().split()))[::-1]
emp_seat = K
ans = 0
while len(A) != 0:
    if emp_seat >= A[-1]:
        emp_seat -= A[-1]
        A.pop()
    else:
        emp_seat = K
        ans += 1
print(ans + 1)

# evima 解説
N, K = map(int, input().split())
A = list(map(int, input().split()))
ans, empty = 0, K
for a in A:
    if a > empty:
        ans += 1
        empty = K - a
    else:
        empty -= a
print(ans + 1)