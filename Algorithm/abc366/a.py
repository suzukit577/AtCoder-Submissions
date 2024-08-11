N, T, A = map(int, input().split())
print("Yes" if abs(T - A) > N - T - A else "No")
