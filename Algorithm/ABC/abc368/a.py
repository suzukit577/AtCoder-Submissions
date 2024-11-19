N, K = map(int, input().split())
A = list(map(int, input().split()))
print(*(A[N - K :] + A[: N - K]))


# evima 解説
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = A[N - K :] + A[: N - K]
print(*B)
