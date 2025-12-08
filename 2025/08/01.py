import math

points = [tuple(map(int, line.split(","))) for line in open("input").readlines()]

def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)

distances = []
for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        distances.append((i, j, dist(points[i], points[j])))

distances.sort(key=lambda x: x[2])

nodes = set()
for node in distances[:1000]:
    nodes.add(node[0])
    nodes.add(node[1])

components = []
while nodes:
    component = set([nodes.pop()])
    modified = True
    while modified:
        modified = False
        for d in distances[:1000]:
            if (d[0] in component) ^ (d[1] in component):
                component.add(d[0])
                component.add(d[1])
                modified = True
    nodes -= component
    components.append(component)

components.sort(key=lambda c: len(c), reverse=True)
total = 1
for component in components[:3]:
    total *= len(component)
print(total)
