S = input()
num_komoji, num_oomoji = 0, 0
for s in S:
    if ord("a") <= ord(s) <= ord("z"):
        num_komoji += 1
    else:
        num_oomoji += 1
print(S.upper() if num_komoji < num_oomoji else S.lower())
