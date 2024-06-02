N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]
get = [0] * M
for i in range(N):
    for j in range(M):
        get[j] += X[i][j]
for i in range(M):
    if get[i] < A[i]:
        print("No")
        break
else:
    print("Yes")

# evima 解説 (栄養素のループを外側にした方が楽)
N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]
ans = True
for j in range(M):
    s = sum(X[i][j] for i in range(N))
    ans &= s >= A[j]
print("Yes" if ans else "No")
