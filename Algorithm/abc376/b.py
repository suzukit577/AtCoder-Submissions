N, Q = map(int, input().split())
l, r = 1, 2
ans = 0
for _ in range(Q):
    H, T = input().split()
    T = int(T)
    if H == "L":
        if l < r < T or T < r < l:
            ans += N - abs(T - l)
        else:
            ans += abs(T - l)
        l = T
    else:
        if r < l < T or T < l < r:
            ans += N - abs(T - r)
        else:
            ans += abs(T - r)
        r = T
print(ans)


# 公式解説
def num_move(N: int, from_: int, to: int, ng: int) -> int:
    if from_ > to:
        from_, to = to, from_
    if from_ < ng < to:
        return N - to + from_
    else:
        return to - from_


N, Q = map(int, input().split())
l, r = 1, 2
ans = 0
for _ in range(Q):
    H, T = input().split()
    T = int(T)
    if H == "L":
        ans += num_move(N, l, T, r)
        l = T
    else:
        ans += num_move(N, r, T, l)
        r = T
print(ans)


# ユーザ解説 (kyopro_friends)
# from が 0 になるように index を振り直す
N, Q = map(int, input().split())
L, R = 1, 2
ans = 0
for _ in range(Q):
    H, T = input().split()
    T = int(T)
    if H == "L":
        to = (T - L) % N
        ng = (R - L) % N
        if ng < to:
            ans += N - to
        else:
            ans += to
        L = T
    else:
        to = (T - R) % N
        ng = (L - R) % N
        if ng < to:
            ans += N - to
        else:
            ans += to
        R = T
print(ans)
