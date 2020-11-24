points = []
for y, line in enumerate(open('input').readlines()):
    for x, c in enumerate(line):
        if c == '#':
            points.append((x, y))

station = (17, 23)
points.remove(station)

def slope(p1, p2):
    return (p1[1] - p2[1]) / (p1[0] - p2[0]) if p1[0] != p2[0] else float('-Inf')

def direction(p1, p2):
    return p1[0] > p2[0] if p1[0] != p2[0] else p2[1] > p1[1]

def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** .5

points = sorted(points, key=lambda p: (direction(station, p), slope(station, p), distance(station, p)))

def blast(points):
    i = 0
    while points:
        point = points[i]
        points.remove(point)
        yield point
        while i < len(points) and slope(station, points[i]) == slope(station, point):
            i += 1
        if i == len(points):
            i = 0

for i, point in enumerate(blast(points)):
    if i == 199:
        print(point[0] * 100 + point[1])
        break