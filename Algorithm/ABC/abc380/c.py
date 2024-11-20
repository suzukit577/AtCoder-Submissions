# submit
N, K = map(int, input().split())
S = input()
ones_blocks = []
i = 0
while i < N:
    if S[i] == "1":
        start = i
        while i < N and S[i] == "1":
            i += 1
        end = i - 1
        ones_blocks.append((start, end))
    else:
        i += 1
k_minus_1_block = ones_blocks[K - 2]
k_block = ones_blocks[K - 1]
ans = list(S)
for i in range(k_block[0], k_block[1] + 1):
    ans[i] = "0"
for i in range(k_block[1] - k_block[0] + 1):
    ans[k_minus_1_block[1] + 1 + i] = "1"
print("".join(ans))


# 公式解説
N, K = map(int, input().split())
S = input()
# split
idx = [0] + [i for i in range(1, N) if S[i - 1] != S[i]] + [N]
splitted_S = [S[idx[i] : idx[i + 1]] for i in range(len(idx) - 1)]
# swap (0 の塊と 1 の塊は交互に現れることに注意)
if S[0] == "0":
    kth_1_idx = 2 * K - 1
else:
    kth_1_idx = 2 * K - 2
splitted_S[kth_1_idx - 1], splitted_S[kth_1_idx] = (
    splitted_S[kth_1_idx],
    splitted_S[kth_1_idx - 1],
)
# join
T = "".join(splitted_S)
print(T)


# 別解 - 問題文に記述されている操作の実装
N, K = map(int, input().split())
K -= 1  # 0-indexed にする
S = input()
l = [i for i in range(N) if S[i] == "1" and (i == 0 or S[i - 1] == "0")]
r = [i for i in range(N) if S[i] == "1" and (i == N - 1 or S[i + 1] == "0")]
T = list(S)
for i in range(r[K - 1] + 1, r[K - 1] + (r[K] - l[K]) + 2):
    T[i] = "1"
for i in range(r[K - 1] + (r[K] - l[K]) + 2, r[K] + 1):
    T[i] = "0"
print("".join(T))


# Run Length Encoding
from typing import Iterable, List, Tuple, TypeVar

T = TypeVar("T")


def run_length_encode(iterable: Iterable[T]) -> List[Tuple[T, int]]:
    """与えられたイテラブルに対してランレングス圧縮を行う
    （イテラブルの長さを N として、計算量は O(N)）

    Args:
        iterable (Iterable[T]): 任意のイテラブルなオブジェクト

    Returns:
        List[Tuple[T, int]]: 要素とその出現回数のペアのリスト
    """
    if not iterable:
        return []

    result = []
    iterator = iter(iterable)
    prev = next(iterator)
    count = 1

    for item in iterator:
        if item == prev:
            count += 1
        else:
            result.append((prev, count))
            prev = item
            count = 1

    result.append((prev, count))  # 最後の要素を追加
    return result


N, K = map(int, input().split())
S = input()
rle_S = run_length_encode(S)
new_rle_S = []
cnt = 0
for char, length in rle_S:
    if char == "1":
        cnt += 1
    if char == "1" and cnt == K:
        popped_cl = new_rle_S.pop()
        new_rle_S.append((char, length))
        new_rle_S.append(popped_cl)
    else:
        new_rle_S.append((char, length))
for char, length in new_rle_S:
    print(char * length, end="")
