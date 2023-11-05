s = [input() for _ in range(8)]
h = 0; w = 0
for i in range(8):
    for j in range(8):
        if s[i][j] == "*":
            h = i; w = j
print(chr(w+ord("a")) + str(8-h))

# 解説
s = [input() for _ in range(8)]
for i in range(8):
    for j in range(8):
        if s[i][j] == "*":
            print(f"{'abcdefgh'[j]}{8-i}")
            exit()