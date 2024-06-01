def operate(A: int, B: int, op: str) -> int:
    if op == "+":
        return A + B
    else:
        return A - B


A, B, C, D = map(int, list(input()))
op = ["+", "-"]
for i in range(2):
    for j in range(2):
        for k in range(2):
            if operate(operate(operate(A, B, op[i]), C, op[j]), D, op[k]) == 7:
                print(f"{A}{op[i]}{B}{op[j]}{C}{op[k]}{D}=7")
                exit()
