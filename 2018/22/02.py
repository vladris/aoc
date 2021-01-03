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
for x in range(target[0] + 21):
    for y in range(target[1] + 21):
        erosion(x, y)

for region in regions:
    regions[region] = [regions[region] % 3, {}]

regions[(0, 0)][1] = {}

queue = [(0, 0, 1, 0)]
best = (target[0] + target[1]) * 7

while queue:
    x, y, item, t = queue.pop(0)
    if t >= best:
        continue
    if item in regions[(x, y)][1] and regions[(x, y)][1][item] <= t:
        continue
    regions[(x, y)][1][item] = t

    if (x, y) == target and item == 1:
        if t < best:
            best = t
        continue

    if (x + 1, y) in regions and regions[(x + 1, y)][0] != item:
        queue.append((x + 1, y, item, t + 1))
    if (x, y + 1) in regions and regions[(x, y + 1)][0] != item:
        queue.append((x, y + 1, item, t + 1))
    if (x - 1, y) in regions and regions[(x - 1, y)][0] != item:
        queue.append((x - 1, y, item, t + 1))
    if (x, y - 1) in regions and regions[(x, y - 1)][0] != item:
        queue.append((x, y - 1, item, t + 1))

    if regions[(x, y)][0] == 0:
        queue.append((x, y, 1 if item == 2 else 2, t + 7))
    elif regions[(x, y)][0] == 1:
        queue.append((x, y, 0 if item == 2 else 2, t + 7))
    elif regions[(x, y)][0] == 2:
        queue.append((x, y, 0 if item == 1 else 1, t + 7))

print(regions[target][1][1])
