n = int(input())
s = input()
for i in range(1, n):
    for j in range(1, n+1):
        if i + j > n:
            print(j-1)
            break
        if s[j-1] == s[j+i-1]:
            print(j-1)
            break