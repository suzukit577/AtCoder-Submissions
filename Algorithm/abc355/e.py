def query(i, j):
    print(f"? {i} {j}", flush=True)
    return int(input().strip())


N, L, R = map(int, input().split())
total_sum_mod = 0

# Calculate the sum from L to R by querying the necessary intervals
current = L
while current <= R:
    for i in range(N + 1):
        span = 1 << i
        if current + span - 1 <= R:
            response = query(i, current // span)
            total_sum_mod += response
            total_sum_mod %= 100
            current += span
            break
        elif current + span // 2 - 1 <= R:
            response = query(i - 1, current // (span // 2))
            total_sum_mod += response
            total_sum_mod %= 100
            current += span // 2
            break

print(f"! {total_sum_mod}", flush=True)
