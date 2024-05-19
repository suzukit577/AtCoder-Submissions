N = int(input())
cards = []
for i in range(N):
    A, C = map(int, input().split())
    cards.append((A, C, i + 1))
cards.sort(key=lambda x: x[0])

stack = []
for card in cards:
    while stack and stack[-1][1] > card[1]:
        stack.pop()
    stack.append(card)

ans = [card[2] for card in stack]
print(len(ans))
print(*sorted(ans))

# evima 解説
N = int(input())
p = []
for i in range(N):
    p.append(list(map(int, input().split())) + [i + 1])
p.sort()
ans = []
min_cost = 10 ** 18
for a, c, i in p[::-1]:
    if c < min_cost:
        min_cost = c
        ans.append(i)
print(len(ans))
print(*sorted(ans))