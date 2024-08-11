def build_3d_cumulative_sum(
    NX: int, NY: int, NZ: int, A: list[list[list[int]]]
) -> list[list[list[int]]]:
    S = [[[0] * (NX + 1) for _ in range(NY + 1)] for _ in range(NZ + 1)]
    for x in range(1, NX + 1):
        for y in range(1, NY + 1):
            for z in range(1, NZ + 1):
                S[x][y][z] = A[x - 1][y - 1][z - 1]
                if x > 1:
                    S[x][y][z] += S[x - 1][y][z]
                if y > 1:
                    S[x][y][z] += S[x][y - 1][z]
                if z > 1:
                    S[x][y][z] += S[x][y][z - 1]
                if x > 1 and y > 1:
                    S[x][y][z] -= S[x - 1][y - 1][z]
                if x > 1 and z > 1:
                    S[x][y][z] -= S[x - 1][y][z - 1]
                if y > 1 and z > 1:
                    S[x][y][z] -= S[x][y - 1][z - 1]
                if x > 1 and y > 1 and z > 1:
                    S[x][y][z] += S[x - 1][y - 1][z - 1]
    return S


def query_3d_cumulative_sum(
    S: list[list[list[int]]], Lx: int, Rx: int, Ly: int, Ry: int, Lz: int, Rz: int
) -> int:
    res = S[Rx][Ry][Rz]
    if Lx > 1:
        res -= S[Lx - 1][Ry][Rz]
    if Ly > 1:
        res -= S[Rx][Ly - 1][Rz]
    if Lz > 1:
        res -= S[Rx][Ry][Lz - 1]
    if Lx > 1 and Ly > 1:
        res += S[Lx - 1][Ly - 1][Rz]
    if Lx > 1 and Lz > 1:
        res += S[Lx - 1][Ry][Lz - 1]
    if Ly > 1 and Lz > 1:
        res += S[Rx][Ly - 1][Lz - 1]
    if Lx > 1 and Ly > 1 and Lz > 1:
        res -= S[Lx - 1][Ly - 1][Lz - 1]
    return res


N = int(input())
A = [[[0] * N for _ in range(N)] for _ in range(N)]
for x in range(N):
    for y in range(N):
        A[x][y] = list(map(int, input().split()))
S = build_3d_cumulative_sum(N, N, N, A)
Q = int(input())
for _ in range(Q):
    Lx, Rx, Ly, Ry, Lz, Rz = map(int, input().split())
    ans = query_3d_cumulative_sum(S, Lx, Rx, Ly, Ry, Lz, Rz)
    print(ans)
