S = input()
diff = []
for i in range(len(S) - 2):
    num = int(S[i : i + 3])
    diff.append(abs(num - 753))
print(min(diff))
