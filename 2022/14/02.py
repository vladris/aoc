x_walls, y_walls, sand = {}, {}, set()
limit = 0
for line in open('input').readlines():
    xy = [tuple(map(int, xy.split(','))) for xy in line.strip().split(' -> ')]
    limit = max(limit, max(xy, key=lambda c: c[1])[1])
    for f, t in zip(xy, xy[1:]):
        if f[0] == t[0]:
            if f[0] not in x_walls:
                x_walls[f[0]] = []
            x_walls[f[0]].append((f[1], t[1]) if f[1] < t[1] else (t[1], f[1]))
        else:
            if f[1] not in y_walls:
                y_walls[f[1]] = []
            y_walls[f[1]].append((f[0], t[0]) if f[0] < t[0] else (t[0], f[0]))

y_walls[limit + 2] = [(-10 ** 10, 10 ** 10)]


def free(x, y):
    if (x, y) in sand:
        return False

    if x in x_walls:
        if any(w[0] <= y <= w[1] for w in x_walls[x]):
            return False

    if y in y_walls:
        if any(w[0] <= x <= w[1] for w in y_walls[y]):
            return False
    
    return True


def fall():
    global limit
    x, y = 500, 0

    while True:
        if free(x, y + 1):
            y += 1
        elif free(x - 1, y + 1):
            x -= 1
            y += 1
        elif free(x + 1, y + 1):
            x += 1
            y += 1
        else:
            sand.add((x, y))
            return


while (500, 0) not in sand:
    fall()

print(len(sand))
