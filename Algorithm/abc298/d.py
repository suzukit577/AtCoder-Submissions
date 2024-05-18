# 動画解説
from collections import deque

Q = int(input())
MOD = 998244353
queue = deque()
queue.append(1)
r = 1
for _ in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        x = s[1]
        queue.append(x)
        r = (r * 10 + x) % MOD
    elif s[0] == 2:
        y = queue.popleft()
        r = (r - y * pow(10, len(queue), MOD)) % MOD
    else:
        print(r)