# 1) 提出コード
def check_condition(a, b):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and b[i][j] == 0:
                return False
    return True

def rotate(a):
    n = len(a)
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[n-1-j][i] = a[i][j]
    return res

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
for _ in range(4):
    if check_condition(A, B):
        print("Yes")
        break
    A = rotate(A)
else:
    print("No")

# 2) ChatGPT
def rotate_matrix(A, B):
    N = len(A)
    for _ in range(4): # 最大で4回回転する
        # Aを回転させた結果をA'とする
        A = [[A[N-1-j][i] for j in range(N)] for i in range(N)]
        # A'の要素の値が1になっている場所に対応するBの要素の値を確認し、Bの対応する要素が1であることを確認する
        flag = True
        for i in range(N):
            for j in range(N):
                if A[i][j] == 1 and B[i][j] != 1:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            return True
    return False

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
result = rotate_matrix(A, B)
if result:
    print("Yes")
else:
    print("No")

# 3) numpy を使用した解法
import numpy as np

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
A = np.array(A)
B = np.array(B)

for _ in range(4):
    flag = True
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1 and B[i][j] == 0:
                flag = False
    if flag:
        print("Yes")
        exit()
    A = np.rot90(A)
print("No")