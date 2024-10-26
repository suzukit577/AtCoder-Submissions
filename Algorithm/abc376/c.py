N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
for i in range(N - 1):
    if A[i + 1] > B[i]:
        print(-1)
        break
else:
    for i in range(N - 1):
        if A[i] > B[i]:
            print(A[i])
            break
    else:
        print(A[-1])


# 公式解説 (二分探索)
N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
ok, ng = 1 << 30, 0


def f(x: int, B: list[int]) -> bool:
    NB = B + [x]
    NB.sort()
    for i in range(N):
        if A[i] > NB[i]:
            return False
    return True


if not f(ok, B):
    print(-1)
    exit()
while ok - ng > 1:
    mid = (ok + ng) // 2
    if f(mid, B):
        ok = mid
    else:
        ng = mid
print(ok)
