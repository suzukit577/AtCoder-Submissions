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
