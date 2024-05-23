a, b = map(int, input().split())
negative_cnt = 0
if a * b < 0:
    print("Zero")
    exit()
for i in range(a, b + 1):
    if i < 0:
        negative_cnt += 1
print("Positive" if negative_cnt % 2 == 0 else "Negative")

# 公式解説
a, b = map(int, input().split())
if 0 < a:
    print("Positive")
elif b < 0:
    if (b - a + 1) % 2 == 0:
        print("Positive")
    else:
        print("Negative")
else:
    print("Zero")
