N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(N-1):
    diff = abs(A[i+1] - A[i])
    if diff != 1:
        if A[i+1] > A[i]:
            ans += [A[i] + j for j in range(diff)]
        elif A[i+1] < A[i]:
            ans += [A[i] - j for j in range(diff)]
    else:
        ans.append(A[i])
ans.append(A[-1])
print(*ans)

# 公式解説
N = int(input())
A = list(map(int, input().split()))
B = []
for i in range(N-1):
    if A[i] <= A[i+1]:
        B += list(range(A[i], A[i+1]))
    elif A[i] > A[i+1]:
        B += list(range(A[i], A[i+1], -1))
B.append(A[-1])
print(*B)

# 原案者の実装
N = int(input())
A = input()
for i in range(N-1):
    print(A[i], end=' ')
    if A[i] < A[i+1]:
        for x in range(A[i]+1, A[i+1]):
            print(x, end=' ')
    else:
        for x in range(A[i]-1, A[i+1], -1):
            print(x, end=' ')
print(A[-1])