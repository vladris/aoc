points = set()
folds = []

with open("input") as f:
    line = f.readline().strip()
    while line:
        points.add(tuple(map(int, line.split(","))))
        line = f.readline().strip()

    line = f.readline().strip()
    while line:
        axis, value = line[11:].split("=")
        folds.append((axis, int(value)))
        line = f.readline().strip()

def foldx(x):
    return {(point[0] if point[0] < x else 2 * x - point[0], point[1]) for point in points}

def foldy(y):
    return {(point[0], point[1] if point[1] < y else 2 * y - point[1]) for point in points}

if folds[0][0] == "x":
    points = foldx(folds[0][1])
else:
    points = foldy(folds[0][1])

print(len(points))
