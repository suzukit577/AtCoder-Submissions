N, K = map(int, input().split())
S = input()
ans, i = 0, 0
while i < N:
    if S[i] == "O":
        if i + K <= N and "X" not in S[i : i + K]:
            ans += 1
            i += K
        else:
            i += 1
    else:
        i += 1
print(ans)


# 別解
N, K = map(int, input().split())
S = input()
ans, i = 0, 0
while i < N:
    if S[i] == "O":
        for j in range(i, i + K):
            if j == N or S[j] == "X":
                i = j
                break
        else:
            ans += 1
            i += K
    else:
        i += 1
print(ans)


# 別解 (ランレングス圧縮)
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
ans = 0
for t in rle_S:
    if t[0] == "O":
        ans += t[1] // K
print(ans)


# 公式解説
N, K = map(int, input().split())
S = list(input())
ans = 0
T = ["O"] * K
for i in range(N - K + 1):
    if S[i : i + K] == T:
        ans += 1
        for j in range(i, i + K):
            S[j] = "X"
print(ans)
