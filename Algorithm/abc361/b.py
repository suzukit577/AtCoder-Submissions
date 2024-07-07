a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())
intersected = (
    False if j <= a or k <= b or l <= c or d <= g or e <= h or f <= i else True
)
print("Yes" if intersected else "No")


# evima 解説
def intersect(l1: int, r1: int, l2: int, r2: int) -> bool:
    return max(l1, l2) < min(r1, r2)


a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())
print(
    "Yes"
    if intersect(a, d, g, j) and intersect(b, e, h, k) and intersect(c, f, i, l)
    else "No"
)
