Q = int(input())
bag, num = [0] * (10**6 + 1), 0
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        x = int(query[-1])
        if bag[x] == 0:
            num += 1
        bag[x] += 1
    if query[0] == "2":
        x = int(query[-1])
        bag[x] -= 1
        if bag[x] == 0:
            num -= 1
    if query[0] == "3":
        print(num)

# evima 解説
Q = int(input())
M = 10**6 + 1

c = [0] * M
k = 0
for _ in range(Q):
    s = input()
    if s[0] == "1":
        _, x = map(int, s.split())
        if c[x] == 0:
            k += 1
        c[x] += 1
    elif s[0] == "2":
        _, x = map(int, s.split())
        c[x] -= 1
        if c[x] == 0:
            k -= 1
    else:
        print(k)
