# def solve(N, K, prescriptions):
#     left = 1  # 初日
#     right = 10**18  # 十分に大きな値で初期化
#     while left < right:
#         mid = (left + right) // 2  # 二分探索で日数を求める
#         required = 0
#         for a, b in prescriptions:
#             if a >= mid:
#                 required += b
#         if required <= K:
#             right = mid
#         else:
#             left = mid + 1
#     return left

# # 入力を受け取る
# N, K = map(int, input().split())
# prescriptions = []
# for _ in range(N):
#     a, b = map(int, input().split())
#     prescriptions.append((a, b))
# # 解法を呼び出して結果を出力
# result = solve(N, K, prescriptions)
# print(result)


# 公式解説
N, K = map(int, input().split())
prescriptions = []
for _ in range(N):
    a, b = map(int, input().split())
    prescriptions.append((a, b))
prescriptions.sort()
total = 0
for i in range(N):
    total += prescriptions[i][1]
if total <= K:
    print(1)
else:
    for i in range(N):
        if total <= K:
            print(prescriptions[i - 1][0] + 1)
            exit()
        total -= prescriptions[i][1]
    print(prescriptions[-1][0] + 1)