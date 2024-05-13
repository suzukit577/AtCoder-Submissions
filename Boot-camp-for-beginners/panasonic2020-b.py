H, W = map(int, input().split())
if (H * W) % 2 == 0:
    ans = (H * W) // 2
else:
    ans = (H * W) // 2 + 1
print(ans)