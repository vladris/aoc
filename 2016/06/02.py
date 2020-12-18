input = open("input").readlines()

counts = [{} for _ in range(8)]

for line in input:
    for i, c in enumerate(line.strip()):
        if c not in counts[i]:
            counts[i][c] = 0
        counts[i][c] += 1

print("".join([min(c.keys(), key=lambda x: c[x]) for c in counts]))