def ceil_to_10_multiplier(n: int) -> int:
    if n % 10 == 0:
        return n
    else:
        return (n // 10 + 1) * 10


food = list()
for _ in range(5):
    food.append(int(input()))
rem = list(map(lambda x: x % 10, food))
min_rem = 10
for r in rem:
    if r != 0 and r < min_rem:
        min_rem = r
if min_rem == 10:
    min_rem = 0
id = rem.index(min_rem)

ans = 0
for i in range(5):
    if i == id:
        ans += food[i]
    else:
        ans += ceil_to_10_multiplier(food[i])
print(ans)

# 公式解説-1 (順列全探索)
import itertools

A = list()
for _ in range(5):
    A.append(int(input()))
P = [i for i in range(5)]
final_answer = 10 ** 6
for p in itertools.permutations(P):
    ans = 0
    for i in range(5):
        while ans % 10 != 0:
            ans += 1
        ans += A[p[i]]
    final_answer = min(final_answer, ans)
print(final_answer)

# 公式解説-2 (最後に注文した方が良さそうなものを求める)
def max_time(x: int) -> int:
    return (x + 9) // 10 * 10


def rem_time(x: int) -> int:
    return max_time(x) - x


A = list()
for _ in range(5):
    A.append(int(input()))
ans = sum(list(map(max_time, A)))
ans -= max(list(map(rem_time, A)))
print(ans)
