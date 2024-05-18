N = int(input())
d = list(map(int, input().split()))
d.sort()
mid = N // 2
print(d[mid] - d[mid - 1])