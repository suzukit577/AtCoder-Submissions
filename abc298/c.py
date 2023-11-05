from collections import defaultdict

N = int(input())
Q = int(input())
q2 = defaultdict(list) # 箱 i に入っているカードを表す辞書型
q3 = defaultdict(set) # カード i が入っている箱を表す辞書型

for q in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        i = query[1]; j = query[2]
        q2[j].append(i) # 箱 j にカード i を追加
        q3[i].add(j) # カード i を箱 j に追加
    elif query[0] == 2:
        i = query[1]
        print(*sorted(q2[i]))
    elif query[0] == 3:
        i = query[1]
        print(*sorted(list(q3[i])))

# 動画解説
N = int(input())
Q = int(input())
M = 200001
box = [[] for _ in range(N+1)]
card = [set() for _ in range(M)]
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        i, j = q[1:]
        box[j].append(i)
        card[i].add(j)
    elif q[0] == 2:
        print(*sorted(box[q[1]]))
    else:
        print(*sorted(card[q[1]]))