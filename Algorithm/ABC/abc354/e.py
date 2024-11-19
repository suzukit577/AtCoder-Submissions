def can_win(cards):
    from functools import lru_cache

    @lru_cache(None)
    def dfs(state):
        n = len(state)
        # 現在の状態でのカードの数
        if n == 0:
            return False  # カードがない状態は負けの状態

        for i in range(n):
            for j in range(i + 1, n):
                if state[i][0] == state[j][0] or state[i][1] == state[j][1]:
                    # 新しい状態を構築
                    new_state = state[:i] + state[i + 1:j] + state[j + 1:]
                    if not dfs(new_state):
                        return True  # 次の状態で相手が負けるなら勝てる

        return False  # どの状態に行っても負けるなら負け

    # 初期状態のカードのペア
    initial_state = tuple((A[i], B[i]) for i in range(N))
    return dfs(initial_state)

# 入力の読み取り
N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

if can_win(list(zip(A, B))):
    print("Takahashi")
else:
    print("Aoki")