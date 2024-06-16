def count_set_bits(n: int) -> int:
    """
    与えられた整数の 2 進数表現において 1 が立っているビットの数をカウントする関数: O(log(n))

    Parameters:
    n (int): 整数

    Returns:
    int: 1 が立っているビットの数
    """
    # nを 2 進数文字列に変換し、'0b' prefix を取り除く
    binary_representation = bin(n)[2:]
    # '1' の数をカウントする
    return binary_representation.count("1")


N, M = map(int, input().split())
S = [input() for _ in range(N)]
ans = 10**7
for mask in range(2**N):
    ok = [False] * M
    for i in range(N):
        if mask & (1 << i):
            for j in range(M):
                if S[i][j] == "o":
                    ok[j] = True
    if sum(ok) == M:
        ans = min(ans, count_set_bits(mask))
print(ans)
