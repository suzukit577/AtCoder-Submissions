H = int(input())
ans = 0
for i in range(10**6):
    ans += 2**i
    H //= 2
    if H <= 0:
        break
print(ans)

# 公式解説
def num_attack(H: int) -> int:
    return 2 * num_attack(H // 2) + 1 if H > 1 else 1


H = int(input())
print(num_attack(H))
