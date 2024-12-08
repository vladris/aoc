locations = {}

lines = [line.strip() for line in open("input").readlines()]

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c.isalnum():
            if c not in locations:
                locations[c] = []
            locations[c].append((i, j))


def get_pairs():
    for key in locations:
        for i in range(len(locations[key])):
            for j in range(i + 1, len(locations[key])):
                yield locations[key][i], locations[key][j]


def in_grid(p):
    return 0 <= p[0] and p[0] < len(lines) and 0 <= p[1] and p[1] < len(lines[0])


result = set()
for p in get_pairs():
    di, dj = p[1][0] - p[0][0], p[1][1] - p[0][1]
    p1 = p[0][0] - di, p[0][1] - dj
    p2 = p[1][0] + di, p[1][1] + dj

    if in_grid(p1):
        result.add(p1)
    if in_grid(p2):
        result.add(p2)

print(len(result))
