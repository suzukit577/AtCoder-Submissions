def carpet_of_level_K(K: int) -> list[str]:
    if K == 0:
        return ["#"]
    else:
        carpet = [["#"] * (3**K) for _ in range(3**K)]
        # 中央のブロックは白
        for i in range(3 ** (K - 1), 2 * (3 ** (K - 1))):
            for j in range(3 ** (K - 1), 2 * (3 ** (K - 1))):
                carpet[i][j] = "."
        # 他の 8 個のブロックはレベル (K - 1) のカーペット
        sub_carpet = carpet_of_level_K(K - 1)
        for i in range(3):
            for j in range(3):
                if (i, j) != (1, 1):
                    for y in range(3 ** (K - 1)):
                        for x in range(3 ** (K - 1)):
                            carpet[i * 3 ** (K - 1) + y][j * 3 ** (K - 1) + x] = (
                                sub_carpet[y][x]
                            )
        return carpet


N = int(input())
carpet = carpet_of_level_K(N)
for i in range(3**N):
    for j in range(3**N):
        print(carpet[i][j], end="")
    print()
