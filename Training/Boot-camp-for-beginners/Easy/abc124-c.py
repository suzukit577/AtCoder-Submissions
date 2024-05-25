S = input()
N = len(S)
tile_0 = "01" * (N // 2) + "0" * (N % 2)
tile_1 = "10" * (N // 2) + "1" * (N % 2)
cnt_0, cnt_1 = 0, 0
for i in range(N):
    if tile_0[i] != S[i]:
        cnt_0 += 1
    if tile_1[i] != S[i]:
        cnt_1 += 1
print(min(cnt_0, cnt_1))
