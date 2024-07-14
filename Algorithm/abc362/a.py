prices = list(map(int, input().split()))
C = input()
if C == "Red":
    print(min(prices[1:]))
if C == "Green":
    print(min(prices[0], prices[2]))
if C == "Blue":
    print(min(prices[:2]))

# 公式解説
R, G, B = map(int, input().split())
C = input()
if C == "Red":
    print(min(G, B))
if C == "Green":
    print(min(B, R))
if C == "Blue":
    print(min(R, G))
