n, q = map(int, input().split())
cnt = 1
st = set()
for _ in range(q):
    e = input()
    if e == "1":
        st.add(cnt)
        cnt += 1
    elif e == "3":
        for m in st: # print(min(st))
            print(m)
            break
    else:
        c, x = e.split()
        st.discard(int(x))

# 解放2: O(q)
n, q = map(int, input().split())
gone = [0] * (n+1)
ans = 1
for _ in range(q):
    event = input()
    if event == "1":
        pass
    elif event[0] == "2":
        c, x = event.split()
        gone[int(x)] = 1
    else:
        while(gone[ans]):
            ans += 1
        print(ans)