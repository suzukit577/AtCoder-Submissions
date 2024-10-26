S = [list(input()) for _ in range(8)]
ng_i, ng_j = set(), set()
for i in range(8):
    for j in range(8):
        if S[i][j] == "#":
            ng_i.add(i)
            ng_j.add(j)
ans = (8 - len(ng_i)) * (8 - len(ng_j))
print(ans)
