N = int(input())
A = [0]
counts = [0] * 200001
for _ in range(N):
    a = int(input())
    A.append(a)
    counts[a] += 1
max_num = max(A)
for i in range(1, N + 1):
    if A[i] == max_num and counts[max_num] == 1:
        for j in range(max_num - 1, 0, -1):
            if counts[j] != 0:
                print(j)
                break
    else:
        print(max_num)

# 公式解説-1
N = int(input())
A = list()
A_sub = list()
for i in range(N):
    a = int(input())
    A.append(a)
    A_sub.append(a)
A_sub.sort()
A_sub.pop()

A_max = max(A)
A_second = max(A_sub)
for a in A:
    if a == A_max:
        print(A_second)
    else:
        print(A_max)

# 公式解説-2
N = int(input())
left = [0] * (N + 2)
right = [0] * (N + 2)
A = [0]
for _ in range(N):
    A.append(int(input()))
A.append(0)

for j in range(1, N + 1):
    left[j] = max(left[j - 1], A[j])
for j in range(N, 0, -1):
    right[j] = max(right[j + 1], A[j])

for i in range(1, N + 1):
    print(max(left[i - 1], right[i + 1]))
