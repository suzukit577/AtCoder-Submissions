def minmax_xcoord_for_free(sx: int, sy: int, ty: int) -> tuple[int, int]:
    if (sx + sy) % 2 == 0:
        return sx - abs(sy - ty), sx + abs(sy - ty) + 1
    else:
        return sx - abs(sy - ty) - 1, sx + abs(sy - ty)


Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())
# 縦方向の移動は必ずコストがかかる
ans = abs(Sy - Ty)
# コストをかけずに移動できるマスの x 座標の最小値と最大値
min_x, max_x = minmax_xcoord_for_free(Sx, Sy, Ty)
# 横方向の移動にコストがかかる場合を反映する
if not min_x <= Tx <= max_x:
    dx = min(abs(Tx - min_x), abs(Tx - max_x))
    if dx % 2 == 1:
        dx += 1
    ans += dx // 2
print(ans)
