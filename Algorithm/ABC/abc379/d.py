import bisect

Q = int(input())
plants = []
offset = 0
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        bisect.insort_right(plants, 0 - offset)
    elif query[0] == "2":
        T = int(query[1])
        offset += T
    elif query[0] == "3":
        H = int(query[1])
        idx = bisect.bisect_left(plants, H - offset)
        print(len(plants) - idx)
        plants = plants[:idx]


# 公式解説
from collections import deque

Q = int(input())
queue = deque()  # 植物が植えられたクエリの番号を管理するキュー
height = [0] * (
    Q + 1
)  # height[i]: 最初に植物が植えられて、それが収穫されずに i 番目のクエリまで処理された場合の高さ
for i in range(Q):
    query = input().split()
    if query[0] == "1":
        height[i + 1] = height[i]
        queue.append(i)
    elif query[0] == "2":
        T = int(query[1])
        height[i + 1] = height[i] + T
    else:
        H = int(query[1])
        height[i + 1] = height[i]
        ans = 0
        while queue:
            idx = queue[0]
            if height[i + 1] - height[idx] >= H:
                ans += 1
                queue.popleft()
            else:
                break
        print(ans)
