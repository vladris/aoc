from itertools import permutations

input = open("input").readlines()

grid = [[c == "." or c.isdigit() for c in line.strip()] for line in input]

dest = {}

for i, line in enumerate(input):
    for j, c in enumerate(line):
        if c.isdigit():
            dest[c] = (j, i)

def dist(x, y):
    visited = {}
    queue = [(x, y, 0)]

    while queue:
        x, y, d = queue.pop(0)

        if x < 0 or len(grid[0]) <= x or y < 0 or len(grid) <= y:
            continue

        if not grid[y][x]:
            continue

        if (x, y) in visited and visited[(x, y)] <= d:
            continue

        visited[(x, y)] = d
        queue.append((x - 1, y, d + 1))
        queue.append((x + 1, y, d + 1))
        queue.append((x, y - 1, d + 1))
        queue.append((x, y + 1, d + 1))

    return visited

dists = {}
for start in dest:
    d = dist(*dest[start])
    dists[dest[start]] = {}
    for end in dest:
        if start == end:
            continue
        dists[dest[start]][dest[end]] = d[dest[end]]

to = sorted(dest.keys())
to.remove("0")

best = 10 ** 6
for perm in permutations(to):
    perm = "0" + "".join(perm) + "0"
    dist = 0
    for a, b in zip(perm, perm[1:]):
        dist += dists[dest[a]][dest[b]]
    best = min(dist, best)

print(best)
