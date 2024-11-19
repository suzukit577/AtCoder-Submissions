N = int(input())
A = list(map(int, input().split()))
ans, left, right = N, 0, 0
while left < N - 1:
    if right < N - 1 and (
        left == right or A[right + 1] - A[right] == A[left + 1] - A[left]
    ):
        right += 1
        ans += (
            right - left
        )  # 左端を A[left] に固定し、右端として A[left + 1], ..., A[right] のいずれかを選んで得られる部分列の個数
    else:
        left += 1
print(ans)

# 公式解説
N = int(input())
A = list(map(int, input().split()))
B = [A[i + 1] - A[i] for i in range(N - 1)]

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


B_enc = run_length_encode(B)
ans = N
for n, c in B_enc:
    ans += c * (c + 1) // 2
print(ans)


# evima 解説
N = int(input())
A = list(map(int, input().split()))
d = [A[i + 1] - A[i] for i in range(N - 1)]
combo, ans = 0, N
for i in range(N - 1):
    if i > 0 and d[i] == d[i - 1]:
        combo += 1
    else:
        combo = 1
    ans += combo
print(ans)
