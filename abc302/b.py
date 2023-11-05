H, W = map(int, input().split())
S = [input() for _ in range(H)]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
for i in range(H):
    for j in range(W):
        if S[i][j] == 's':
            for k in range(8):
                string = ''
                for t in range(5):
                    y = i + t * dy[k]
                    x = j + t * dx[k]
                    if y < 0 or y >= H or x < 0 or x >= W:
                        break
                    string += S[y][x]
                if string == 'snuke':
                    for t in range(5):
                        y = i + t * dy[k]
                        x = j + t * dx[k]
                        print(y + 1, x + 1)
                    exit()