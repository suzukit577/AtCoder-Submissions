# これだと TLE する
def solve(graph, ans_list):
    t, a, b = map(int, input().split())
    a -= 1; b -= 1
    if t == 1:
        if b not in graph[a]:
            graph[a].add(b)
    elif t == 2:
        if b in graph[a]:
            graph[a].remove(b)
    else:
        if b in graph[a] and a in graph[b]:
            ans_list.append("Yes")
        else:
            ans_list.append("No")

n, q = map(int, input().split())
graph = [[] for _ in range(n)]
ans_list = []
for _ in range(q):
    solve(graph, ans_list)
for ans in ans_list:
    print(ans)