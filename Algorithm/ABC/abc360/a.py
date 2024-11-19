S = input()
print("Yes" if S.index("R") < S.index("M") else "No")

# evima 解説
import re

S = input()
print("Yes" if re.search("R.*M", S) else "No")
