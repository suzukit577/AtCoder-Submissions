N = int(input())
H = list(map(int, input().split()))
H[0] -= 1
for i in range(1, N - 1):
    if H[i] - 1 >= H[i - 1]:
        H[i] -= 1
print("Yes" if H == sorted(H) else "No")

# 公式解説 (右のマスから順に操作する, 左から順に行っても同様)
N = int(input())
H = list(map(int, input().split()))
for i in range(N - 2, 0, -1):
    if H[i] <= H[i + 1]:
        pass
    elif H[i] - 1 == H[i + 1]:
        H[i] -= 1
    else:
        print("No")
        exit()
print("Yes")

# 公式解説 (別解)
N = int(input())
H = list(map(int, input().split()))
Mi = 0
for i in range(N):
    Mi = max(H[i], Mi)
    if H[i] < Mi - 1:
        print("No")
        break
else:
    print("Yes")
