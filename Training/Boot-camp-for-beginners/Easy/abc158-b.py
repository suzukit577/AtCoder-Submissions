N, A, B = map(int, input().split())
q, r = N // (A + B), N % (A + B)
ans = q * A + r if r <= A else (q + 1) * A
print(ans)
