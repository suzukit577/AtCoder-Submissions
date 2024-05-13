H, W = map(int, input().split())
if H == 1 or W == 1:
    ans = 1
elif H % 2 == 0 or W % 2 == 0:
    ans = (H * W) // 2
else:
    ans = (H * W) // 2 + 1
print(ans)