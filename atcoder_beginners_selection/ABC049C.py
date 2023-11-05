s = input()
s_rev = s[::-1]
s_dev = ["dream", "dreamer", "erase", "eraser"]
s_dev_rev = [s_dev[i][::-1] for i in range(4)]

can = True
i = 0
while(i < len(s)):
    can2 = False
    for j in range(4):
        if s_rev[i:i+len(s_dev_rev[j])] == s_dev_rev[j]:
            can2 = True
            i += len(s_dev_rev[j])
    if not can2:
        can = False
        break

if can:
    print("YES")
else:
    print("NO")