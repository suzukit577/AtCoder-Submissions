# N = int(input())
# cards = [(0, 0, 0) for _ in range(N)]
# for i in range(N):
#     A, C = map(int, input().split())
#     cards[i] = (A, C, i + 1)
# cards.sort(key=lambda x: x[0])
# ans = []
# for i in range(N - 1):
#     if cards[i][0] < cards[i + 1][0] and cards[i][1] < cards[i + 1][1]:
#         ans.append(cards[i][2])
# ans.append(cards[-1][2])
# print(len(ans))
# print(*sorted(ans))

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