S = input()
cond1 = S[0] == "A"
cond2 = S[2:-1].count("C") == 1
SS = set(S)
SS.discard("A")
SS.discard("C")
cond3 = SS == {s.lower() for s in SS}
print("AC" if cond1 and cond2 and cond3 else "WA")
