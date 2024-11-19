def run_length_encoding(s: str) -> list[str, int]:
    """Run Length Encoding: O(n)

    Args:
        s (str): str

    Returns:
        list: list of tuple which elements are character in given string and number of it
    """
    n = len(s)
    ans = []  # 圧縮後のリスト
    l = 0  # 始点
    while l < n:
        r = l + 1
        while r < n and s[l] == s[r]:  # 異なる文字になるまで進む
            r += 1
        ans.append((s[l], r - l))  # 文字, 連続する個数
        l = r  # 連続しなかった文字から探索を開始
    return ans


S = input()
ans = run_length_encoding(S)
for a in ans:
    print(*a, end=" ")
