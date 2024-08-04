Y = int(input())
if Y % 4 != 0:
    print(365)
elif Y % 4 == 0 and Y % 100 != 0:
    print(366)
elif Y % 100 == 0 and Y % 400 != 0:
    print(365)
elif Y % 400 == 0:
    print(366)

# evima 解説
Y = int(input())
if Y % 4 != 0 or (Y % 100 == 0 and Y % 400 != 0):
    print(365)
else:
    print(366)
