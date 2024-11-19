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


# evima 解説
Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())

# 入力は x, y 座標が両方偶数なら左、そうでないなら右側にある
# S, T 両方の入力を左側に揃えておく
Sx -= (Sy - Sx) % 2
Tx -= (Ty - Tx) % 2

# (Sx, Sy) を原点とするように (Tx, Ty) を移動
Tx -= Sx
Ty -= Sy

# (Tx, Ty) を第一象限に持ってくる
Tx = abs(Tx)
Ty = abs(Ty)

print(Ty + max(0, Tx - Ty) // 2)
