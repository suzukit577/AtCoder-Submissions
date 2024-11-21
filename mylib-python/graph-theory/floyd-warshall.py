# Floyd–Warshall Algorithm: O(N^3)
def Floyd_Warshall(dist: list[list[int]]) -> list[list[int]]:
    N = len(dist)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
