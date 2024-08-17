A, B, C = map(int, input().split())
if B < C:
    print("Yes" if A < B or C < A else "No")
else:
    print("Yes" if not B < A < 24 and not 0 <= A < C else "No")

# evima 解説
A, B, C = map(int, input().split())
if B < C:
    print("No" if B < A < C else "Yes")
else:
    print("Yes" if C < A < B else "No")
