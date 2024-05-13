A, B = map(int, input().split())
ans, plugs = 0, 1
while plugs < B:
    plugs += A - 1
    ans += 1
print(ans)