N = input()
num_digits = len(N)
ans = int(N[0]) + 9 * (num_digits - 1)
if num_digits > 1 and not all(n == "9" for n in N[1:]):
    ans -= 1
print(ans)
