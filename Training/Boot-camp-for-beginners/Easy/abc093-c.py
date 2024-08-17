A, B, C = sorted(map(int, input().split()))
ans = 0
if (3 * C) % 2 == (A + B + C) % 2:
    # できるだけ 2 を足して増やす
    ans += (C - B) // 2 + (C - A) // 2
    # 足りない分を帳尻合わせる
    ans += (C - B) % 2
else:
    # できるだけ 2 を足して増やしたあと、最小のものに 2 を加えて他の 2 つに 1 を加える
    ans += (C - B) // 2 + (C - A) // 2 + 2
print(ans)
