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
    
    t = p[0]
    while in_grid(t):
        result.add(t)
        t = t[0] - di, t[1] - dj
    
    t = p[1]
    while in_grid(t):
        result.add(t)
        t = t[0] + di, t[1] + dj

print(len(result))
