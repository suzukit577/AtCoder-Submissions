N = int(input())
A = list(map(int, input().split()))
A.sort()
Alice, Bob = 0, 0
for i in range(N // 2):
    Alice += A.pop()
    Bob += A.pop()
if len(A) != 0:
    Alice += A.pop()
print(Alice - Bob)