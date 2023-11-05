n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
A = a[::2]
B = a[1::2]
print(sum(A) - sum(B))