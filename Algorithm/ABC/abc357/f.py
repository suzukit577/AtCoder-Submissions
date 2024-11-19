# evima 解説
from atcoder.lazysegtree import LazySegTree

N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353


class Elem:
    def __init__(self, a, b, c, s):
        self.a = a % MOD
        self.b = b % MOD
        self.c = c % MOD
        self.s = s % MOD


class Func:
    def __init__(self, a, b):
        self.a = a % MOD
        self.b = b % MOD


t = LazySegTree(
    lambda l, r: Elem(l.a + r.a, l.b + r.b, l.c + r.c, l.s + r.s),
    Elem(0, 0, 0, 0),
    lambda f, x: Elem(
        x.a + x.c * f.a,
        x.b + x.c * f.b,
        x.c,
        x.s + x.a * f.b + x.b * f.a + x.c * f.a * f.b,
    ),
    lambda f, g: Func(f.a + g.a, f.b + g.b),
    Func(0, 0),
    [Elem(a, b, 1, a * b) for a, b in zip(A, B)],
)

for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        l, r, x = map(int, q[1:])
        t.apply(l - 1, r, Func(x, 0))
    elif q[0] == "2":
        l, r, x = map(int, q[1:])
        t.apply(l - 1, r, Func(0, x))
    else:
        l, r = map(int, q[1:])
        print(t.prod(l - 1, r).s)
