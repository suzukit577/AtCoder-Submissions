# 公式解説
from heapq import heappush, heappop
import sys

input = sys.stdin.readline


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
            nd = d + weight
            if dist[u] > nd:
                dist[u] = nd
                heappush(pq, (nd, u))
    return dist


N, M = map(int, input().split())
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    U, V, B = map(int, input().split())
    U -= 1
    V -= 1
    G[U].append((V, B + A[V]))
    G[V].append((U, B + A[U]))
dist = dijkstra(G, 0)
for i in range(N):
    dist[i] += A[0]
print(*dist[1:])
