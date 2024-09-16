N, M = map(int, input().split())
has_first_boy = [False] * N
for _ in range(M):
    A, B = input().split()
    A = int(A)
    if not has_first_boy[A - 1] and B == "M":
        print("Yes")
        has_first_boy[A - 1] = True
    else:
        print("No")

# evima 解説
N, M = map(int, input().split())
t = [0] * (N + 1)
for _ in range(M):
    A, B = input().split()
    A = int(A)
    if B == "M" and t[A] == 0:
        print("Yes")
        t[A] = 1
    else:
        print("No")
