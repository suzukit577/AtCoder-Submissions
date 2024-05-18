H = int(input())
ans = 0
i = 0
height = 0
while True:
    height += 2 ** i
    i += 1
    ans += 1
    if height > H:
        print(ans)
        exit()