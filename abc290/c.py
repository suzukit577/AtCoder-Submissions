import sys

n, k = map(int, input().split())
a = set(map(int, input().split()))
for i in range(k):
    if i not in a:
        print(i)
        sys.exit()
print(k)