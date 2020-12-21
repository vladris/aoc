import re

input = open("input").read().strip().split("\n\n")

tiles = []

def flip(grid):
    return [line[::-1] for line in grid]

def rotate(grid):
    rgrid = []
    for i in range(len(grid[0])):
        rgrid.append("".join(reversed([line[i] for line in grid])))
    return rgrid

def opp(d):
    return "nesw"[("nesw".index(d) + 2) % 4]

class Tile:
    def __init__(self, grid, id):
        self.id = id
        self.grid = grid
        self.neighbors = {}

    def border(self, d):
        if d == "n":
            return self.grid[0]
        elif d == "e":
            return str("".join([line[-1] for line in self.grid]))
        elif d == "s":
            return self.grid[-1]
        elif d == "w":
            return str("".join([line[0] for line in self.grid]))

    def fix(self, b, d):
        if d in self.neighbors:
            return

        for _ in range(2):
            for _ in range(4):
                self.grid = rotate(self.grid)
                if self.border(d) == b:
                    return
            self.grid = flip(self.grid)

    def connect(self):
        for d in "nesw":
            if d in self.neighbors:
                continue

            for tile in tiles:
                if tile == self:
                    continue

                if not tile.neighbors:
                    tile.fix(self.border(d), opp(d))

                if tile.border(opp(d)) != self.border(d):
                    continue

                self.neighbors[d], tile.neighbors[opp(d)] = tile, self
                tile.connect()
                break

    def line(self, i):
        n = self.neighbors["e"] if "e" in self.neighbors else None
        return self.grid[i][1:-1] + (n.line(i) if n else "")

    def print(self):
        text = []
        for i in range(1, len(self.grid) - 1):
            text.append(self.line(i))

        if "s" in self.neighbors:
            text += self.neighbors["s"].print()

        return text

for tile in input:
    id, rest = tile.split("\n", 1)
    tiles.append(Tile(rest.split("\n"), int(id[5:9])))

t = tiles[0]
t.fix(t.border("s"), "n")
t.connect()

while "n" in t.neighbors:
    t = t.neighbors["n"]
while "w" in t.neighbors:
    t = t.neighbors["w"]

def monster(grid, x, y):
    if x < 18 or y > len(grid) - 2:
        return grid

    points = [(0, 0), (-18, 1), (-13, 1), (-12, 1), (-7, 1), (-6, 1), (-1, 1), (0, 1), (1, 1), (-17, 2), (-14, 2), (-11, 2), (-8, 2), (-5, 2), (-2, 2)]
    for dx, dy in points:
        if grid[y + dy][x + dx] not in "#O":
            return grid

    for dx, dy in points:
        grid[y + dy] = grid[y + dy][:x + dx] + "O" +grid[y + dy][x + dx + 1:]
    return grid

text = t.print()
for _ in range(2):
    for _ in range(4):
        text = rotate(text)
        for y in range(len(text)):
            for x in range(len(text[0])):
                text = monster(text, x, y)

    text = flip(text)

total = 0
for line in text:
    total += sum([c == "#" for c in line])

print(total)
