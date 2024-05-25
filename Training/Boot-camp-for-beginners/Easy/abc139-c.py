N = int(input())
H = list(map(int, input().split()))
can_descend = [False] * N
for i in range(N):
    if i != N - 1 and H[i] >= H[i + 1]:
        can_descend[i] = True
cnt_list = []
for i in range(N):
    if i == 0:
        tmp_cnt = 0
    if can_descend[i] == True:
        tmp_cnt += 1
    else:
        cnt_list.append(tmp_cnt)
        tmp_cnt = 0
print(max(cnt_list))

# ユーザ解説 (TLE)
N = int(input())
H = list(map(int, input().split()))
checked = [False] * N
ans = 0
for i in range(N):
    if not checked[i]:
        checked[i] = True
        for j in range(i + 1, N):
            if H[j - 1] < H[j]:
                break
            checked[j] = True
            ans = max(ans, j - i)
print(ans)
