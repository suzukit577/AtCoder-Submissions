N = int(input())
S = [input() for _ in range(N)]
print(S.count("Takahashi"))

# 別解
N = int(input())
ans = 0
for _ in range(N):
    ans += input() == "Takahashi"
print(ans)
