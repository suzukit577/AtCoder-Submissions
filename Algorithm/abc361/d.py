# evima 解説
from collections import deque

N = int(input()) + 2
S = input() + ".."
T = input() + ".."

d = {S: 0}
q = deque([S])
ans = -1
while q:
    s = q.popleft()
    if s == T:
        ans = d[s]
        break
    empty = s.find(".")
    for i in range(N - 1):
        if "." not in s[i : i + 2]:
            t = list(s)
            t[empty : empty + 2] = t[i : i + 2]
            t[i : i + 2] = [".", "."]
            t = "".join(t)
            if t not in d:
                d[t] = d[s] + 1
                q.append(t)
print(ans)
