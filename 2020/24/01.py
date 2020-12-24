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

print(len(tiles))
