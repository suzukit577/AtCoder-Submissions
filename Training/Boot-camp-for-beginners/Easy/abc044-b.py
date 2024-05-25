from collections import defaultdict

W = input()
cnt_dict = defaultdict(int)
for w in W:
    cnt_dict[w] += 1
for v in cnt_dict.values():
    if v % 2 == 1:
        print("No")
        break
else:
    print("Yes")
