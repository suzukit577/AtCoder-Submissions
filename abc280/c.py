s = input()+'0'
t = input()
n = 0

for i in range(len(t)):
    if s[i] != t[i]:
        n = i
        break

print(n+1)