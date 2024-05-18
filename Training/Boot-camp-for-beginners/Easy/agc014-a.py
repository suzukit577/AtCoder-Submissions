A, B, C = map(int, input().split())
if A == B == C and A % 2 == 0:
    print(-1)
elif A == B == C and A % 2 == 1:
    print(0)
else:
    takahashi, aoki, sunuke = A, B, C
    cnt = 0
    while takahashi % 2 == 0 and aoki % 2 == 0 and sunuke % 2 == 0:
        next_takahashi = (aoki + sunuke) // 2
        next_aoki = (takahashi + sunuke) // 2
        next_sunuke = (takahashi + aoki) // 2
        takahashi, aoki, sunuke = next_takahashi, next_aoki, next_sunuke
        cnt += 1
    print(cnt)
