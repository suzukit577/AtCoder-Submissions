# 公式解説
"""
・f(x) := 睡眠記録を取り始めてから x 分後までに何分寝たか (0 <= x <= A_N)
を求めることができたら，クエリの答えは f(r_i) - f(l_i) として計算できる．
f(x) は A_i <= x <= A_{i+1} の範囲では一次関数になっていることに注意すると，次のような方針で f(x) の値が高速に求められる．

1) 事前に f(A_i) (1 <= i <= N) の値をすべて求めておく．
2) A_j <= x <= A_{j+1} となるような j の値を求める．
3) f(A_j), f(A_{j+1}) の値から f(x) の値を求める．

f(A_i) (1 <= i <= N) の値は，i の照準に計算することで全体で O(N) 時間で求められる．
A_j <= x <= A_{j+1} であるような j は二分探索を使って O(logN) 時間で求められる．
f(x) = f(A_j) + (x - A_j) ((f(A_{j+1}) - f(A_j)) / (A_{j+1} - A_j)) の計算は定数時間で可能．
よって，この問題を O(N + QlogN) 時間で解くことができる．
"""
from bisect import bisect_right

# f(x) := x 分までに何分寝たか
def f(x: int) -> int:
    j = bisect_right(A, x) - 1
    if j == len(fA) - 1:
        return fA[j]
    else:
        return int(fA[j] + ((fA[j + 1] - fA[j]) / (A[j + 1] - A[j])) * (x - A[j]))

N = int(input())
A = list(map(int, input().split()))
fA = [0] * N
for i in range(1, N):
    if i % 2 == 0:
        fA[i] = fA[i - 1] + A[i] - A[i - 1]
    else:
        fA[i] = fA[i - 1]
Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(f(r) - f(l))