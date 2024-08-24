N = int(input())
H = list(map(int, input().split()))
T = 0
for i in range(N):
    if T % 3 == 1:
        T += 1
        H[i] -= 1
        if H[i] <= 0:
            continue
        T += 1
        H[i] -= 3
        if H[i] <= 0:
            continue
    elif T % 3 == 2:
        T += 1
        H[i] -= 3
        if H[i] <= 0:
            continue
    T += 3 * (H[i] // 5)
    if H[i] % 5 <= 2:
        T += H[i] % 5
    else:
        T += 3
    H[i] = 0
print(T)
