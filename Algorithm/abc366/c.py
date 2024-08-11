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
