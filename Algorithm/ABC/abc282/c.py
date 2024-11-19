n = int(input())
s = input().replace(',', '.')
s = list(s)

i = 0
while i < n-1:
    if s[i] == '\"':
        for j in range(i+1, n):
            if s[j] == '\"':
                for k in range(i, j):
                    if s[k] == '.':
                        s[k] = ','
                i = j + 1
                break
    else:
        i += 1


s = "".join(s)
print(s)