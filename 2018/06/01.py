input = open("input").readlines()

ps = {tuple(map(int, line.split(","))) for line in input}

minx, miny, maxx, maxy = 10 ** 6, 10 ** 6, 0, 0
for p in ps:
    if p[0] < minx: minx = p[0]
    if p[0] > maxx: maxx = p[0]
    if p[1] < miny: miny = p[1]
    if p[1] > maxy: maxy = p[1]

dx, dy = maxx - minx, maxy - miny

def closest(x, y):
    bp, bd = set(), 10 ** 6
    for px, py in ps:
        d = abs(px - x) + abs(py - y)
        if d < bd:
            bp = {(px, py)}
            bd = d
        elif d == bd:
            bp = set()
    return bp

inf = set()
for x in range(minx - dx, maxx + dx):
    inf = inf.union(closest(x, miny - dy))
    inf = inf.union(closest(x, maxy + dy))
for y in range(miny - dy, maxy + dy):
    inf = inf.union(closest(minx - dx, y))
    inf = inf.union(closest(maxx + dx, y))

fin = ps - inf
best = 0
for px, py in fin:
    d, count, dc = 1, 1, 1
    while dc:
        dc = 0
        for x in range(px - d, px + d + 1):
            if (px, py) in closest(x, py - d):
                dc += 1
            if (px, py) in closest(x, py + d):
                dc += 1
        for y in range(py - d + 1, py + d):
            if (px, py) in closest(px - d, y):
                dc += 1
            if (px, py) in closest(px + d, y):
                dc += 1
        count += dc
        d += 1
    best = max(best, count)

print(best)
