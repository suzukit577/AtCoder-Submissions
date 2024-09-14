N, M = map(int, input().split())
boys = [[] for _ in range(N)]
ans = ["No" for _ in range(M)]
for i in range(M):
    A, B = input().split()
    A = int(A)
    if not boys[A - 1] and B == "M":
        ans[i] = "Yes"
        boys[A - 1].append(B)
for a in ans:
    print(a)


N, M = map(int, input().split())
has_first_boy = [False] * N
for _ in range(M):
    A, B = input().split()
    A = int(A)
    if B == "M":
        if not has_first_boy[A - 1]:
            print("Yes")
            has_first_boy[A - 1] = True
        else:
            print("No")
    else:
        print("No")
