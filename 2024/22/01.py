nums = [int(line.strip()) for line in open("input").readlines()]

def step(n):
    n = ((n * 64) ^ n) % 16777216
    n = ((n // 32) ^ n) % 16777216
    n = ((n * 2048) ^ n) % 16777216
    return n

total = 0
for n in nums:
    for _ in range(2000):
        n = step(n)
    total += n

print(total)
