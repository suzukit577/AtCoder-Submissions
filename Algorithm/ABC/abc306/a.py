N = int(input())
S = input()
ans = ''
for s in S:
    ans += 2 * s
print(ans)

# 公式解説
N = int(input())
S = input()
for i in range(N):
    print(2 * S[i], end='')
print()

# 公式解説
N = int(input())
S = input()
for s in S:
    print(2 * s, end='')
print()

# その他の実装
N = int(input())
S = input()
print(''.join(c + c for c in S))