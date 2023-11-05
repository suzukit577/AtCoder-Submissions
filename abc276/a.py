# s = input()
# k = -1
# i = len(s) - 1
# while i >= 0:
#     if s[i] == 'a':
#         k = i+1
#         break
#     i -= 1
# print(k)

def main():
    s = input()
    n = len(s)
    for i in range(n, 0, -1):
        if s[i - 1] == 'a':
            print(i)
            return
    print(-1)

main()