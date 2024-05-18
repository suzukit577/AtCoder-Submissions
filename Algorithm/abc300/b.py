def eqaul_matrix(A, B):
    H, W = len(A), len(A[0])
    for i in range(H):
        for j in range(W):
            if A[i][j] != B[i][j]:
                return False
    return True

def left_shift_matrix(A):
    H, W = len(A), len(A[0])
    for i in range(H):
        A[i] = A[i][1:] + A[i][:1]

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]
for i in range(H):
    A = A[1:] + A[:1]
    for j in range(W+1):
        if eqaul_matrix(A, B):
            print("Yes")
            exit()
        left_shift_matrix(A)
print("No")

# 公式解説
H, W = map(int, input().split())
A = [input() for _ in range(H)]
B = [input() for _ in range(H)]
for s in range(H):
    for t in range(W):
        ok = 1
        for i in range(H):
            for j in range(W):
                if A[(i - s) % H][(j - t) % W] != B[i][j]:
                    ok = 0
        if ok:
            print("Yes")
            exit()
print("No")