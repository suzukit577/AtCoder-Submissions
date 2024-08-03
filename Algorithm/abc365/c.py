def can_distribute(x: int, A: list[int], M: int) -> bool:
    total = 0
    for a in A:
        total += min(x, a)
        if total > M:
            return False
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
