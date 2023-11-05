import sys
sys.setrecursionlimit(10**6)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(i: int, j: int) -> None:
    seen[i][j] = True
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if ni < 0 or ni >= H or nj < 0 or nj >= W:
            continue
        if S[ni][nj] != next[S[i][j]]:
            continue
        if seen[ni][nj]:
            continue
        dfs(ni, nj)

H, W = map(int, input().split())
S = [input() for _ in range(H)]
if S[0][0] != 's':
    print('No')
    exit()
next = dict()
next['s'] = 'n'
next['n'] = 'u'
next['u'] = 'k'
next['k'] = 'e'
next['e'] = 's'
seen = [[False] * W for _ in range(H)]
dfs(0, 0)
print('Yes' if seen[H - 1][W - 1] else 'No')