S = set(input())
alphabet = [chr(i) for i in range(ord("a"), ord("z") + 1)]
for a in alphabet:
    if a not in S:
        print(a)
        break
else:
    print("None")

# 公式解説
S = input()
found = [False] * 26
for s in S:
    found[ord(s) - ord("a")] = True
for i in range(26):
    if found[i] == False:
        print(chr(ord("a") + i))
        break
else:
    print("None")
