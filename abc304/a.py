N = int(input())
S = []; A = []
for _ in range(N):
    s, a = input().split()
    a = int(a)
    S.append(s); A.append(a)
n = A.index(min(A))
for i in range(n, N):
    print(S[i])
for i in range(n):
    print(S[i])

# 公式解説
"""
1) まず，N 人全員の年齢を順に調べて，最も若い人の番号 p を求め，
2) その後，人 p から時計回りに N 人全員の名前を出力する．
人 p 自身を 0 番目と起算した時の，人 p から時計回りで i 番目の人の番号は (p + i) mod N と表すことができる．
"""
N = int(input())
S = []; A = []
for _ in range(N):
    s, a = input().split()
    S.append(s); A.append(int(a))
p = A.index(min(A))
for i in range(N):
    print(S[(p + i) % N])