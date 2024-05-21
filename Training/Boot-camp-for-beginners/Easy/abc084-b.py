A, B = map(int, input().split())
S = input()
numbers = set([str(i) for i in range(10)])
head = set(S[:A])
tail = set(S[A + 1 :])
flag = True if head <= numbers and tail <= numbers and S[A] == "-" else False
print("Yes" if flag else "No")
