pos = list(map(int, open("input").readline().split(",")))

total = 10 ** 8
for p in range(max(pos)):
    total = min(total, sum([(abs(p - t) * (abs(p - t) + 1) // 2) for t in pos]))

print(total)
