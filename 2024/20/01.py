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

shortcuts = 0

def cheat(i, j, dx, dy):
    global shortcuts
    if (i + dx, j + dy) in dist and dist[(i + dx, j + dy)] < dist[(i, j)] - 2:
        d = dist[(i, j)] - dist[(i + dx, j + dy)] - 2
        if d >= 100:
            shortcuts += 1


for i, j in dist:
    for (dx, dy) in [(-2, 0), (2, 0), (0, -2), (0, 2), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        cheat(i, j, dx, dy)

print(shortcuts)
