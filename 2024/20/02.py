grid = [line.strip() for line in open("input").readlines()]

for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == "S":
            start = (i, j)
        elif char == "E":
            end = (i, j)

dist, at = {end: 0}, end
while at != start:
    i, j = at
    if (i - 1, j) not in dist and grid[i - 1][j] != "#":
        dist[(i - 1, j)] = dist[at] + 1
        at = (i - 1, j)
    elif (i + 1, j) not in dist and grid[i + 1][j] != "#":
        dist[(i + 1, j)] = dist[at] + 1
        at = (i + 1, j)
    elif (i, j - 1) not in dist and grid[i][j - 1] != "#":
        dist[(i, j - 1)] = dist[at] + 1
        at = (i, j - 1)
    else:
        dist[(i, j + 1)] = dist[at] + 1
        at = (i, j + 1)

def candidates(i, j):
    for si, sj in dist:
        if si == i and sj == j:
            continue
        if abs(si - i) + abs(sj - j) <= 20:
            yield si, sj


shortcuts = 0
for i, j in dist:
    for si, sj in candidates(i, j):
        d = dist[(i, j)] - dist[(si, sj)] - (abs(si - i) + abs(sj - j))
        if d >= 100:
            shortcuts += 1

print(shortcuts)
