def is_in_24_hours(h, m):
    return 0 <= h <= 23 and 0 <= m <= 59

def misjudged(h, m):
    A, B = h // 10, h % 10  # hの10の位と1の位
    C, D = m // 10, m % 10  # mの10の位と1の位
    AC = A * 10 + C         # 入れ替えた後の時
    BD = B * 10 + D         # 入れ替えた後の分
    return is_in_24_hours(AC, BD)

H, M = map(int, input().split())
while not misjudged(H, M):
    M += 1
    if M == 60:
        H, M = H + 1, 0
    if H == 24:
        H = 0
print(H, M)