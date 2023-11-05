N, M, H, K = map(int, input().split())
S = input()
item = {tuple(map(int, input().split())) for _ in range(M)}
x, y = 0, 0
for s in S:
    if s == 'R': x += 1
    if s == 'L': x -= 1
    if s == 'U': y += 1
    if s == 'D': y -= 1
    H -= 1
    if H < 0:
        print('No')
        exit()
    if H < K and (x, y) in item:
        item.discard((x, y))
        H = K
print('Yes')