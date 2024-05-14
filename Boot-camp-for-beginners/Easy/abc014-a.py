A, B, C = map(int, input().split())
if A == B == C:
    print(-1)
else:
    takahashi, aoki, sunuke = A, B, C
    cnt = 0
    while takahashi % 2 == 0 and aoki % 2 == 0 and sunuke % 2 == 0:
        next_takahashi = aoki // 2 + sunuke // 2
        next_aoki = takahashi // 2 + sunuke // 2
        next_sunuke = takahashi // 2 + aoki // 2
        takahashi = next_takahashi
        aoki = next_aoki
        sunuke = next_sunuke
        cnt += 1
    print(cnt)