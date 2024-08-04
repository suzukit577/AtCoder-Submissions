def can_distribute(x: int, A: list[int], M: int) -> bool:
    total = 0
    for a in A:
        total += min(x, a)
    return total <= M


N, M = map(int, input().split())
A = list(map(int, input().split()))
if sum(A) <= M:
    print("infinite")
else:
    left, right = 0, max(A)
    while left <= right:
        mid = (left + right) // 2
        if can_distribute(mid, A, M):
            left = mid + 1
        else:
            right = mid - 1
    print(right)


# evima 解説
N, M = map(int, input().split())
A = list(map(int, input().split()))
if sum(A) <= M:
    print("infinite")
    exit()


def cond(x: int) -> bool:
    s = sum(min(x, a) for a in A)
    return s <= M


ok, ng = 0, max(A)
while ok + 1 < ng:
    mi = (ok + ng) // 2
    if cond(mi):
        ok = mi
    else:
        ng = mi
print(ok)
