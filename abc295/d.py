s = input()
table = [0 for _ in range(2**10)] # 分布のリスト
table[0] = 1
bit = 0
for i in range(len(s)):
    si = int(s[i])
    # ここまでの 0~9 までの偶奇を bit で表現
    bit ^= 2**si # 排他的論理和
    table[bit] += 1
ans = 0
# 同じ偶奇を持つ個数の組み合わせを計上
for t in table:
    # 組み合わせのコンビネーションの公式
    ans += t * (t-1) // 2
print(ans)