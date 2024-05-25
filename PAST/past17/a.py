H, W = map(int, input().split())
H /= 100
BMI = W / (H**2)
if BMI < 20:
    print("A")
elif BMI < 25:
    print("B")
else:
    print("C")
