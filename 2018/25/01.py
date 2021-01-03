input = open("input").readlines()

constellations = []

for line in input:
    x, y, z, w = tuple(map(int, line.split(",")))
    matches = []
    for constellation in constellations:
        for px, py, pz, pw in constellation:
            if abs(x - px) + abs(y - py) + abs(z - pz) + abs(w - pw) <= 3:
                matches.append(constellation)
                break

    if not matches:
        constellations.append({ (x, y, z, w) })
        continue

    while len(matches) > 1:
        matches[0].update(matches[1])
        matches[1].clear()
        matches.pop(1)

    matches[0].add((x, y, z, w))
    constellations = list(filter(None, constellations))

print(len(constellations))
