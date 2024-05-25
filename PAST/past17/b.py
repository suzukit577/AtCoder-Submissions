N = int(input())
strings = set()
for _ in range(N):
    strings.add(input())
if strings == {"Perfect"}:
    print("All Perfect")
elif strings == {"Perfect", "Great"} or strings == {"Great"}:
    print("Full Combo")
else:
    print("Failed")
