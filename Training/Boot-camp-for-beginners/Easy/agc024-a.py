# 漸化式を立てて解く
A, B, C, K = map(int, input().split())
if abs(A - B) > 10**18:
    print("Unfair")
elif K % 2 == 0:
    print(A - B)
else:
    print(B - A)
