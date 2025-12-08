import math

points = [tuple(map(int, line.split(","))) for line in open("input").readlines()]

def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)

distances = []
for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        distances.append((i, j, dist(points[i], points[j])))

distances.sort(key=lambda x: x[2])

def solve(points, distances):
    components = [set([i]) for i in range(len(points))]
    for d in distances:
        for c in components:
            if d[0] in c:
                comp_a = c
            if d[1] in c:
                comp_b = c
        if comp_a != comp_b:
            if len(components) == 2:
                return points[d[0]][0] * points[d[1]][0]
            comp_a |= comp_b
            components.remove(comp_b)

print(solve(points, distances))
