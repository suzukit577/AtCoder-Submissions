from collections import defaultdict

n, q = map(int, input().split())
follows = defaultdict(int)
ans_list = []
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        follows[(a,b)] = 1
    elif t == 2:
        follows[(a,b)] = 0
    else:
        if follows[(a,b)] == 1 and follows[(b,a)] == 1:
            ans_list.append("Yes")
        else:
            ans_list.append("No")
for ans in ans_list:
    print(ans)