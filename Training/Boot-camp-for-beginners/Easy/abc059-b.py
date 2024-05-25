A = input()
B = input()
if len(A) > len(B):
    print("GREATER")
    exit()
elif len(A) < len(B):
    print("LESS")
    exit()
else:
    N = len(A)
    for i in range(N):
        if int(A[i]) > int(B[i]):
            print("GREATER")
            exit()
        elif int(A[i]) < int(B[i]):
            print("LESS")
            exit()
    print("EQUAL")
