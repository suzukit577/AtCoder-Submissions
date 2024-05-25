N = int(input())
W_list, W_set = list(), set()
flag = True
for i in range(N):
    w = input()
    if W_list and w[0] != W_list[-1][-1] or w in W_set:
        flag = False
    W_list.append(w)
    W_set.add(w)
print("Yes" if flag else "No")
