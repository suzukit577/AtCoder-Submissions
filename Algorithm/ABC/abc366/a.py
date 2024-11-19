N, T, A = map(int, input().split())
print("Yes" if abs(T - A) > N - T - A else "No")

# evima 解説
N, T, A = map(int, input().split())
if max(T, A) > N // 2:
    print("Yes")
else:
    print("No")

# 公式解説
n, t, a = map(int, input().split())
if a >= (n + 1) // 2 or t >= (n + 1) // 2:
    print("Yes")
else:
    print("No")
