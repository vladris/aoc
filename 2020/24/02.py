import re

input = open("input").readlines()

tiles = set()

for line in input:
    q, r = 0, 0
    for m in re.finditer(r"(e|w|se|sw|ne|nw)", line):
        if m[0] == "e":
            q += 1
        elif m[0] == "w":
            q -= 1
        elif m[0] == "se":
            r += 1 
        elif m[0] == "sw":
            q -= 1
            r += 1
        elif m[0] == "ne":
            q += 1
            r -= 1
        elif m[0] == "nw":
            r -= 1

    if (q, r) in tiles:
        tiles.remove((q, r))
    else:
        tiles.add((q, r))

def neighbors(q, r):
    yield q + 1, r
    yield q - 1, r
    yield q, r + 1
    yield q, r - 1
    yield q - 1, r + 1
    yield q + 1, r - 1

def count(q, r, tiles):
    n = 0
    for qn, rn in neighbors(q, r):
        if (qn, rn) in tiles:
            n += 1
    return n

for _ in range(100):
    new_tiles = []
    for q, r in tiles:
        if 0 < count(q, r, tiles) < 3:
            new_tiles.append((q, r))

        for qn, rn in neighbors(q, r):
            if (qn, rn) not in tiles and count(qn, rn, tiles) == 2:
                new_tiles.append((qn, rn))
    tiles = set(new_tiles)

print(len(tiles))
