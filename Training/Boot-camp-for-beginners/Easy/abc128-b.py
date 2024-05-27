N = int(input())
restaurants = list()
for i in range(N):
    S, P = input().split()
    restaurants.append((S, int(P), i + 1))
restaurants.sort(key=lambda x: (x[0], -x[1]))
for i in range(N):
    print(restaurants[i][-1])
