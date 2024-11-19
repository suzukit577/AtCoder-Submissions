# TLE コード
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
N, cnt = len(rle_S), 0
used = [False] * N
for i in range(N):
    if rle_S[i][0] == "1":
        cnt += 1
    if rle_S[i][0] == "1" and cnt == K - 1:
        new_rle_S.append(rle_S[i])
        used[i] = True
        for j in range(i + 1, N):
            if rle_S[j][0] == "1":
                new_rle_S.append(rle_S[j])
                cnt += 1
                used[j] = True
                break
    elif not used[i]:
        new_rle_S.append(rle_S[i])
ans = ""
for rle in new_rle_S:
    ans += rle[0] * rle[1]
print(ans)


# AC コード
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


# 別解 - 問題文に記述されている操作の実装
