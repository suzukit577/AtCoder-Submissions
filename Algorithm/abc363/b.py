N, T, P = map(int, input().split())
L = list(map(int, input().split()))
L.sort(reverse=True)
if L[P - 1] >= T:
    print(0)
else:
    print(T - L[P - 1])
