Q, H, S, D = map(int, input().split())
N = int(input())
ans = 0
cost_2L = min(D, S * 2, H * 4, Q * 8)
cost_1L = min(S, H * 2, Q * 4)
ans = (N // 2) * cost_2L + (N % 2) * cost_1L
print(ans)
