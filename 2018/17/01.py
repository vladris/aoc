import re

lines = open("input").readlines()

minx, maxx, miny, maxy = 10 ** 6, 0, 10 ** 6, 0

hlines, vlines = [], []
slines, flines = [], []

visited = set()

for line in lines:
    m = re.match(r"(x|y)=(\d+), (x|y)=(\d+)..(\d+)", line)
    if m[1] == "x":
        vlines.append((int(m[2]), int(m[4]), int(m[5])))
        miny = min(miny, int(m[4]))
        maxy = max(maxy, int(m[5]))
        minx = min(minx, int(m[2]))
        maxx = max(maxx, int(m[2]))
    else:
        hlines.append((int(m[2]), int(m[4]), int(m[5])))
        miny = min(miny, int(m[2]))
        maxy = max(maxy, int(m[2]))
        minx = min(minx, int(m[4]))
        maxx = max(maxx, int(m[5]))

def inhline(x, y, lines):
    for ly, lx1, lx2 in lines:
        if y == ly and lx1 <= x <= lx2:
            return True
    return False

def invline(x, y):
    for lx, ly1, ly2 in vlines:
        if x == lx and ly1 <= y <= ly2:
            return True
    return False

def vflow(x, y):
    global maxy, visited

    while not inhline(x, y, hlines + slines + flines) and y <= maxy:
        visited.add((x, y))
        y += 1

    if y > maxy or inhline(x, y, flines):
        return []

    return [(hflow, x, y - 1)]

def hflow(x, y):
    result = []

    lx, rx = x, x
    while not invline(lx, y) and inhline(lx, y + 1, hlines + slines):
        visited.add((lx, y))
        lx -= 1
    if not inhline(lx, y + 1, hlines + slines):
        result.append((vflow, lx, y + 1))

    while not invline(rx, y) and inhline(rx, y + 1, hlines + slines):
        visited.add((rx, y))
        rx += 1
    if not inhline(rx, y + 1, hlines + slines):
        result.append((vflow, rx, y + 1))

    if result:
        flines.append((y, lx, rx))
        return result
    else:
        slines.append((y, lx, rx))
        return [(hflow, x, y - 1)]

def count():
    grid = [["."] * (maxx - minx + 3) for _ in range(maxy + 1)]

    for x, y in visited:
        grid[y][x - minx + 1] = "|"

    for y, x1, x2 in flines:
        for x in range(x1, x2 + 1):
            grid[y][x - minx + 1] = "|"

    for y, x1, x2 in slines:
        for x in range(x1, x2 + 1):
            grid[y][x - minx + 1] = "~"

    for x, y1, y2 in vlines:
        for y in range(y1, y2 + 1):
            grid[y][x - minx + 1] = "#"

    for y, x1, x2 in hlines:
        for x in range(x1, x2 + 1):
            grid[y][x - minx + 1] = "#"

    grid[0][500 - minx + 1] = "+"

    total = 0
    for line in grid:
        for c in line:
            if c in "~|":
                total += 1

    return total

queue = vflow(500, miny)
while queue:
    flow, x, y = queue.pop()
    queue += flow(x, y)

print(count())
