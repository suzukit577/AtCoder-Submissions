def check_bingo(bingo: list[list[bool]]) -> bool:
    for i in range(3):
        if bingo[i][0] and bingo[i][1] and bingo[i][2]:
            return True
        elif bingo[0][i] and bingo[1][i] and bingo[2][i]:
            return True
    if bingo[0][0] and bingo[1][1] and bingo[2][2]:
        return True
    elif bingo[0][2] and bingo[1][1] and bingo[2][0]:
        return True
    else:
        return False

A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
bingo = [[False] * 3 for _ in range(3)]
b = [int(input()) for _ in range(N)]
for i in range(N):
    for j in range(3):
        for k in range(3):
            if A[j][k] == b[i]:
                bingo[j][k] = True
if check_bingo(bingo):
        print('Yes')
else:
    print('No')