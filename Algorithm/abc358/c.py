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


# evima 解説 (ビット全探索, 自分の提出と同じ方針)
N, M = map(int, input().split())
S = [input() for _ in range(N)]

s = [0] * N  # 種類ごとにポップコーンを販売しているかをビットマスクで管理
for i in range(N):
    for j in range(M):
        if S[i][j] == "o":
            s[i] |= 1 << j  # ビット単位論理和

ans = N
for mask in range(1 << N):
    o = 0
    for i in range(N):
        if mask >> i & 1:
            o |= s[i]  # 訪れる店舗で売っているポップコーンを記録
    if o == (1 << M) - 1:
        ans = min(ans, bin(mask).count("1"))
print(ans)


# evima 解説 (深さ優先探索)
def dfs(cur: int, mask: int) -> int:
    """
    cur は現在の店舗のインデックスを表します。
    mask は現在までに販売されたポップコーンの種類をビットマスクで表します。

    ベースケース：
    cur が N（全店舗数）に達した場合、全店舗をチェックし終えたことを意味します。
    すべてのポップコーンの種類が販売されているかを確認します。
    -   mask == (1 << M) - 1 は、mask のすべてのビットが 1 であることを確認します。
        これは全ての種類のポップコーンが販売されたことを意味します。
    -   全ての種類が販売されていれば 0（必要な店舗数は0）、
        そうでなければ N（無理なケースを示す大きな値）を返します。

    再帰的ステップ：
    次の店舗（cur + 1）に進む二つの選択肢を考えます：
    -   現在の店舗を選び、その店舗の販売状況をビットマスクに加える場合：
        dfs(cur + 1, mask | s[cur]) + 1
        -   mask | s[cur] は現在のマスクに現在の店舗の販売状況を加える操作です。
        -   この場合、店舗を1つ使うので結果に +1 します。
    -   現在の店舗を選ばない場合：dfs(cur + 1, mask)
        -   mask はそのままです。
    上記の二つの選択肢のうち、必要な店舗数が少ない方を選びます。
    """
    if cur == N:
        return 0 if mask == (1 << M) - 1 else N
    return min(dfs(cur + 1, mask | s[cur]) + 1, dfs(cur + 1, mask))


N, M = map(int, input().split())
S = [input() for _ in range(N)]

s = [0] * N  # 種類ごとにポップコーンを販売しているかをビットマスクで管理
for i in range(N):
    for j in range(M):
        if S[i][j] == "o":
            s[i] |= 1 << j  # ビット単位論理和

"""
DFS 関数を初期状態（最初の店舗 0、まだ販売されたポップコーンの種類は 0）で呼び出し、
その結果を出力します。
"""
print(dfs(0, 0))
