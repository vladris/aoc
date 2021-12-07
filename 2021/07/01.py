pos = list(map(int, open("input").readline().split(",")))

total = 10 ** 6
for p in range(max(pos)):
    total = min(total, sum([abs(p - t) for t in pos]))

print(total)
