# Dijkstra's Algorithm: O((V+E)log(V))
from heapq import heappop, heappush


def dijkstra(graph: list[list[tuple[int, int]]], start: int) -> list[int]:
    """
    ダイクストラ法: O((V+E)log(V))

    入力:
    graph (list[list[tuple[int, int]]]): 非負重み付き（無向/有向）グラフの隣接リスト,
    start (int): 開始ノード

    出力:
    dist: 開始ノードから各ノード (0, 1, ..., V) への最短経路長からなるリスト
    """
    INF = 10**18
    dist = [INF] * len(graph)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, v = heappop(pq)
        if d > dist[v]:
            continue
        for u, weight in graph[v]:
            new_d = d + weight
            if dist[u] > new_d:
                dist[u] = new_d
                heappush(pq, (new_d, u))
    return dist
