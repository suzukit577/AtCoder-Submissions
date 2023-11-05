N = int(input())
l, r = 0, N - 1
for i in range(20):
    m = (l + r) // 2
    print('?', m + 1)
    res = int(input())
    if res == 0:
        l = m
    else:
        r = m
    if r - l == 1:
        print('!', l + 1)
        break