n, x = map(int, input().split())
a = set(map(int, input().split()))
flag = False
for ai in a:
    if ai - x in a:
        print("Yes")
        exit()
print("No")

# 尺取法 (ソート + 線形時間)
n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
i = 0
for j in range(n):
    while i < n and a[i] - a[j] < x:
        i += 1
    if i < n and a[i] - a[j] == x:
        print("Yes")
        exit()
print("No")