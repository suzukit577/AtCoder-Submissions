def inner_product(a: list[int], b: list[int]) -> int:
    res, N = 0, len(a)
    for i in range(N):
        res += a[i] * b[i]
    return res


xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

vec_ab, vec_ac = [xb - xa, yb - ya], [xc - xa, yc - ya]
vec_bc, vec_ba = [xc - xb, yc - yb], [xa - xb, ya - yb]
vec_ca, vec_cb = [xa - xc, ya - yc], [xb - xc, yb - yc]

if (
    inner_product(vec_ab, vec_ac) == 0
    or inner_product(vec_bc, vec_ba) == 0
    or inner_product(vec_ca, vec_cb) == 0
):
    print("Yes")
else:
    print("No")


# 別解 (三平方の定理)
xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())
sqlen_ab, sqlen_bc, sqlen_ca = (
    (xb - xa) ** 2 + (yb - ya) ** 2,
    (xc - xb) ** 2 + (yc - yb) ** 2,
    (xa - xc) ** 2 + (ya - yc) ** 2,
)
if (
    sqlen_ab == sqlen_bc + sqlen_ca
    or sqlen_bc == sqlen_ca + sqlen_ab
    or sqlen_ca == sqlen_ab + sqlen_bc
):
    print("Yes")
else:
    print("No")

# 公式解説
xA, yA = map(int, input().split())
xB, yB = map(int, input().split())
xC, yC = map(int, input().split())
AB2 = (xA - xB) ** 2 + (yA - yB) ** 2
BC2 = (xB - xC) ** 2 + (yB - yC) ** 2
CA2 = (xC - xA) ** 2 + (yC - yA) ** 2
if AB2 + BC2 == CA2 or BC2 + CA2 == AB2 or CA2 + AB2 == BC2:
    print("Yes")
else:
    print("No")
