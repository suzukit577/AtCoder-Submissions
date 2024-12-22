numbers = list(map(int, input().split()))
if numbers[0] == numbers[1] == numbers[2]:
    print("Yes")
else:
    C = max(numbers)
    numbers.remove(C)
    if sum(numbers) == C:
        print("Yes")
    else:
        print("No")
