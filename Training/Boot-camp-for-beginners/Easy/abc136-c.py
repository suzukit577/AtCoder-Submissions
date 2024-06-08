N = int(input())
H = list(map(int, input().split()))
H[0] -= 1
for i in range(1, N - 1):
    if H[i] - 1 >= H[i - 1]:
        H[i] -= 1
print("Yes" if H == sorted(H) else "No")
