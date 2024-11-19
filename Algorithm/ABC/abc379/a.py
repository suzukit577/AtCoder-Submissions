N = input()
print(N[1] + N[2] + N[0], N[2] + N[0] + N[1])


# 公式解説 - 実装方針1 (入力を1文字毎に受け取る)
a, b, c = input()
print(f"{b}{c}{a} {c}{a}{b}")


# 公式解説 - 実装方針2 (整数 N を整数型として受け取る)
N = int(input())
a = N // 100
b = (N // 10) % 10
c = N % 10
print(f"{b}{c}{a} {c}{a}{b}")
