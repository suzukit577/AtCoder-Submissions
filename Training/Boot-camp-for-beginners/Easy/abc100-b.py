D, N = map(int, input().split())
if D == 0:
    nums = list(range(100)) + [101]
    print(nums[N])
if D == 1:
    nums = list(range(0, 10000, 100)) + [10100]
    print(nums[N])
if D == 2:
    nums = list(range(0, 1000000, 10000)) + [1010000]
    print(nums[N])
