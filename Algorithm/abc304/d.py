# 公式解説
from collections import defaultdict
from bisect import bisect

W, H = map(int, input().split())
N = int(input())
p = [0] * N; q = [0] * N
for i in range(N): p[i], q[i] = map(int, input().split())
A = int(input())
a = list(map(int, input().split()))
a.append(W)
B = int(input())
b = list(map(int, input().split()))
b.append(H)

dd = defaultdict(int)
for i in range(N):
    X = bisect(a, p[i])
    Y = bisect(b, q[i])
    dd[(X, Y)] += 1

M = max(dd.values())
if len(dd.keys()) == (A + 1) * (B + 1):
    m = min(dd.values())
else:
    m = 0

print(m, M)