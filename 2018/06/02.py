input = open("input").readlines()

ps = {tuple(map(int, line.split(","))) for line in input}

minx, miny, maxx, maxy = 10 ** 6, 10 ** 6, 0, 0
for p in ps:
    if p[0] < minx: minx = p[0]
    if p[0] > maxx: maxx = p[0]
    if p[1] < miny: miny = p[1]
    if p[1] > maxy: maxy = p[1]

dx, dy = maxx - minx, maxy - miny

def distance(x, y):
    total = 0
    for px, py in ps:
        total += abs(px - x) + abs(py - y)
    return total

total = 0
for x in range(minx - dx, maxx + dx):
    for y in range(miny - dy, maxy + dy):
        if distance(x, y) < 10000:
            total += 1

print(total)
