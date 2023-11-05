h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
ans = 0
for order in range(2**(h+w-2)): # 経路全列挙
    hi, wj = 0, 0
    seen = set()
    seen.add(a[0][0])
    for i in range(h+w-2):
        if order >> i & 1:
            hi += 1
            if hi == h: # 盤外
                break
            if a[hi][wj] in seen: # 嬉しくない
                break
        else:
            wj += 1
            if wj == w: # 盤外
                break
            if a[hi][wj] in seen: # 嬉しくない
                break
        seen.add(a[hi][wj])
    else:
        ans += 1
print(ans)