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

# 公式解説
import calendar

Y = int(input())
print(366 if calendar.isleap(Y) else 365)

# 公式解説 (別解)
from datetime import date

Y = int(input())
print((date(Y + 1, 1, 1) - date(Y, 1, 1)).days)
