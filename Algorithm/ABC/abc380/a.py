N = input()
print("Yes" if N.count("1") == 1 and N.count("2") == 2 and N.count("3") == 3 else "No")


# 公式解説 - 解法1: 各桁に何が何文字含まれるか数える
N = int(input())
mem = [0] * 10
while N > 0:
    mem[N % 10] += 1
    N //= 10
print("Yes" if mem[1] == 1 and mem[2] == 2 and mem[3] == 3 else "No")


# 公式解説 - 解法2: 各桁をソートして 122333 と一致するか判定
N = input()
print("Yes" if "".join(sorted(N)) == "122333" else "No")
