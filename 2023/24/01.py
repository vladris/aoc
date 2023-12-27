class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy


min_bounds = 200000000000000
max_bounds = 400000000000000

hails = []
for line in open('input').readlines():
    pos, vec = line.strip().split(' @ ')
    x, y, _ = tuple(map(int, pos.split(', ')))
    dx, dy, _ = tuple(map(int, vec.split(', ')))
    hails.append((Point(x, y), Vector(dx, dy)))


def intersect(p1, v1, p2, v2):
    if v1.dx / v1.dy == v2.dx / v2.dy:
        return None, None

    t2 = (v1.dx * (p2.y - p1.y) + v1.dy * (p1.x - p2.x)) / (v2.dx * v1.dy - v2.dy * v1.dx)
    t1 = (p2.y + v2.dy * t2 - p1.y) / v1.dy

    return t1, t2


total = 0
for i1 in range(len(hails) - 1):
    for i2 in range(i1 + 1, len(hails)):
        h1, h2 = hails[i1], hails[i2]
        t1, t2 = intersect(*h1, *h2)

        if not t1 or not t2:
            continue

        if t1 < 0 or t2 < 0:
            continue

        x, y = h1[0].x + h1[1].dx * t1, h1[0].y + h1[1].dy * t1
        if (min_bounds <= x <= max_bounds) and (min_bounds <= y <= max_bounds):
            total += 1

print(total)
