N, M = map(int, input().split())
correct = [False] * N
wrong = [0] * N
for _ in range(M):
    p, S = input().split()
    p = int(p)
    if S == "AC":
        correct[p - 1] = True
    elif S == "WA" and not correct[p - 1]:
        wrong[p - 1] += 1
penalty = 0
for i in range(N):
    if correct[i]:
        penalty += wrong[i]
print(sum(correct), penalty)
