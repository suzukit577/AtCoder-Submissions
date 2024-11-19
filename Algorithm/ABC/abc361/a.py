N, K, X = map(int, input().split())
A = list(map(int, input().split()))
print(*(A[:K] + [X] + A[K:]))

# evima 解説
N, K, X = map(int, input().split())
A = list(map(int, input().split()))
A.insert(K, X)
print(*A)
