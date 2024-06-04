from collections import defaultdict

N = int(input())
cnt_dict = defaultdict(int)
for _ in range(N):
    cnt_dict[input()] += 1
M = int(input())
for _ in range(M):
    cnt_dict[input()] -= 1
max_value = max(cnt_dict.values())
print(max_value if max_value >= 0 else 0)


# ユーザ解説
N = int(input())
S = []
for _ in range(N):
    S.append(input())
M = int(input())
T = []
for _ in range(M):
    T.append(input())
ans = 0
for s in S:
    point = 0
    for j in range(N):
        if S[j] == s:
            point += 1
    for j in range(M):
        if T[j] == s:
            point -= 1
    ans = max(ans, point)
print(ans)
