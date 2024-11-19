dist = [0, 3, 4, 8, 9, 14, 23]
p, q = input().split()
if p > q:
    p, q = q, p
p_num = ord(p) - ord('A')
q_num = ord(q) - ord('A')
print(dist[q_num] - dist[p_num])

# 公式解説
# 推奨しない解法：答えを全部埋め込んでしまう

# 実装例1 - 辺の長さを for-loop 等を用いて足し合わせ
p, q = input().split()
p_num = ord(p) - ord('A')
q_num = ord(q) - ord('A')
if p_num > q_num:
    p_num, q_num = q_num, p_num
e = [3, 1, 4, 1, 5, 9]
ans = 0
for i in range(p_num, q_num):
    ans += e[i]
print(ans)

# 実装例2 - A から G を何らかの座標に対応させる
"""
A を数直線上の x = 0 の地点とみなして，B から G までの座標を計算すると
順に x = 3, 4, 8, 9, 14, 23 になる．このとき地点間の距離は座標の差の
絶対値になるので，abs 関数を利用して計算できる．
"""
p, q = input().split()
e = [0, 3, 4, 8, 9, 14, 23]
print(abs(e[ord(p) - ord('A')] - e[ord(q) - ord('A')]))

# 楽な実装
"""
各文字間の距離が小さいので，文字列の形で直接書いてしまい，出現位置を検索して差を調べることで答えを求めることができる
"""
p, q = input().split()
s = 'A..BC...DE....F........G'
print(abs(s.find(p) - s.find(q)))