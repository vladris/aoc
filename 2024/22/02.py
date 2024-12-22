nums = [int(line.strip()) for line in open("input").readlines()]

def step(n):
    d = n % 10
    n = ((n * 64) ^ n) % 16777216
    n = ((n // 32) ^ n) % 16777216
    n = ((n * 2048) ^ n) % 16777216
    return n, n % 10 - d + 9


buys, seq = {}, set()
for i, n in enumerate(nums):
    buys[i] = {}
    n, d1 = step(n)
    n, d2 = step(n)
    n, d3 = step(n)
    change = d1 * 19 ** 2 + d2 * 19 + d3
    for _ in range(1997):
        n, d = step(n)
        change = (change % 19 ** 3) * 19 + d
        seq.add(change)
        if change not in buys[i]:
            buys[i][change] = n % 10

best = 0
for s in seq:
    total = 0
    for i in range(len(nums)):
        if s in buys[i]:
            total += buys[i][s]
    best = max(total, best)

print(best)
