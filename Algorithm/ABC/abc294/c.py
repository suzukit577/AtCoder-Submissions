n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = sorted(a + b)
sa = set(a); sb = set(b)
id_a = []; id_b = []
for i in range(n+m):
    if c[i] in sa:
        id_a.append(i+1)
    else:
        id_b.append(i+1)
print(*id_a)
print(*id_b)

# get_index = {ci: i + 1 for i, ci in enumerate(c)}
# for ai in a:
#     print(get_index[ai])
# for bi in b:
#     print(get_index[bi])