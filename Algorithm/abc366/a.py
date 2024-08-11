N, T, A = map(int, input().split())
print("Yes" if abs(T - A) > N - T - A else "No")

# evima 解説
N, T, A = map(int, input().split())
if max(T, A) > N // 2:
    print("Yes")
else:
    print("No")
