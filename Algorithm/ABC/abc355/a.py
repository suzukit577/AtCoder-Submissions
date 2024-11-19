A, B = map(int, input().split())
print(-1 if A == B else 6 - A - B)

# evima 解説
A, B = map(int, input().split())
s = set([1, 2, 3])
s.discard(A)
s.discard(B)
print(s.pop() if len(s) == 1 else -1)
