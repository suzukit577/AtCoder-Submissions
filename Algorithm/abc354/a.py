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

# evima 解説
H = int(input())
x = 0
for i in range(99):
    x += 2 ** i
    if x > H:
        print(i + 1)
        break