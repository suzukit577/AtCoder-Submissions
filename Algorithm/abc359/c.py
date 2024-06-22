def minmax_horizontal_for_free(sx: int, sy: int, ty: int) -> tuple[int, int]:
    pos = "left" if (sx + sy) % 2 == 0 else "right"
    if pos == "left":
        return sx - abs(sy - ty), sx + abs(sy - ty) + 1
    else:
        return sx - abs(sy - ty) - 1, sx + abs(sy - ty)


Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())
# 縦方向の移動は必ずコストがかかる
ans = abs(Sy - Ty)
# コストをかけずに移動できるマスの x 座標の最小値と最大値
min_horizontal, max_horizontal = minmax_horizontal_for_free(Sx, Sy, Ty)
# 横方向の移動にコストがかかる場合を反映する
if not min_horizontal <= Tx <= max_horizontal:
    dx = 0
    if Sx < Tx:
        dx = Tx - max_horizontal
        if dx % 2 == 1:
            dx += 1
    else:
        dx = min_horizontal - Tx
        if dx % 2 == 1:
            dx += 1
    ans += dx // 2
print(ans)
