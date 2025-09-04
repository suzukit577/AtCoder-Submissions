N = int(input())
a = [int(input()) - 1 for _ in range(N)]
cur, cnt, visited = 0, 0, set()
for _ in range(N):
    if a[cur] == 1:
        break
    if a[cur] in visited:
        print(-1)
        exit()
    visited.add(cur)
    cur = a[cur]
    cnt += 1
print(cnt + 1)

# 公式解説
N = int(input())
a = [int(input()) - 1 for _ in range(N)]
now, c = 0, 0
while True:
    if now == 1:
        print(c)
        break
    if c >= N:
        print(-1)
        break
    c += 1
    now = a[now]

# 別解 - 1
N = int(input())
a = [int(input()) - 1 for _ in range(N)]
cur = 0
for i in range(N):
    cur = a[cur]
    if cur == 1:
        print(i + 1)
        exit()
print(-1)

# 別解 - 2
N = int(input())
a = [int(input()) - 1 for _ in range(N)]
res, cur = 0, 0
seen = [False for _ in range(N)]
while cur != 1:
    seen[cur] = True
    cur = a[cur]
    res += 1
    if seen[cur]:
        print(-1)
        exit()
print(res)
