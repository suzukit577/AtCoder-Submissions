N = int(input())
events = []
for _ in range(N):
    l, r = map(int, input().split())
    events.append((l, "start"))
    events.append((r, "end"))
events.sort(
    key=lambda x: (x[0], x[1] == "end")
)  # 開始点と終了点が同じ場合は "start" を優先する
current_intervals = 0
intersections = 0
for event in events:
    if event[1] == "start":
        intersections += current_intervals
        current_intervals += 1
    else:
        current_intervals -= 1
print(intersections)
