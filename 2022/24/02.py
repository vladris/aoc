import math

blizzards = []
lines = [line.strip() for line in open('input').readlines()]
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c in '<^>v':
            blizzards.append((x, y, c))

maxx, maxy = len(lines[0]) - 1, len(lines) - 1
move = {'<': (-1, 0), '^': (0, -1), '>': (1, 0), 'v': (0, 1)}


def step(blizzards):
    new = []
    for b in blizzards:
        x, y = b[0] + move[b[2]][0], b[1] + move[b[2]][1]
        if x == 0: x = maxx - 1
        if x == maxx: x = 1
        if y == 0: y = maxy - 1
        if y == maxy: y = 1
        new.append((x, y, b[2]))
    return new


def occupancy(blizzards):
    return {(x, y) for x, y, c in blizzards}


steps, lcm = {}, math.lcm(maxx - 1, maxy - 1)
for i in range(lcm):
    steps[i] = {(x, y) for x, y, _ in blizzards}
    blizzards = step(blizzards)


def solve(src, dest, step):
    queue = [(src[0], src[1], step)]
    while True:
        x, y, step = queue.pop(0)
        
        for x, y in [(x + m[0], y + m[1]) for m in move.values()] + [(x, y)]:
            if (x, y) == (dest[0], dest[1]):
                return step + 1

            if (x, y) != (src[0], src[1]):
                if x <= 0 or x >= maxx or y <= 0 or y >= maxy:
                    continue

            if (x, y) in steps[(step + 1) % lcm]:
                continue

            if (x, y, step + 1) not in queue:
                queue.append((x, y, step + 1))


trip1 = solve((1, 0), (maxx - 1, maxy), 0)
trip2 = solve((maxx - 1, maxy), (1, 0), trip1)
trip3 = solve((1, 0), (maxx - 1, maxy), trip2)
print(trip3)
