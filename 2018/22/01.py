target = (9, 751)
depth = 11817

regions = {
    (0, 0): depth % 20183,
    target: depth % 20183
}

def erosion(x, y):
    global target

    if (x, y) in regions:
        return regions[(x, y)]
    if y == 0:
        e = x * 16807
    elif x == 0:
        e = y * 48271
    else:
        e = erosion(x - 1, y) * erosion(x, y - 1)

    e = (e + depth) % 20183
    regions[(x, y)] = e
    return e

risk = 0
for x in range(target[0] + 1):
    for y in range(target[1] + 1):
        risk += erosion(x, y) % 3

print(risk)
