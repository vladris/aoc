class Cuboid:
    def __init__(self, x, y, z, on):
        self.x0, self.x1 = max(x[0], -50), min(x[1], 50)
        self.y0, self.y1 = max(y[0], -50), min(y[1], 50)
        self.z0, self.z1 = max(z[0], -50), min(z[1], 50)
        self.on = on

    def mark(self, grid):
        for dx in range(self.x0, self.x1 + 1):
            for dy in range(self.y0, self.y1 + 1):
                for dz in range(self.z0, self.z1 + 1):
                    grid[dx + 50][dy + 50][dz + 50] = self.on

def coord(s):
    return tuple(map(int, s[2:].split("..")))

cuboids = []
for line in open("input").readlines():
    c = line[3:].strip().split(",")
    cuboids.append(Cuboid(coord(c[0]), coord(c[1]), coord(c[2]), line.startswith("on")))

grid = [[[False] * 101 for _ in range(101)] for _ in range(101)]
for cuboid in cuboids:
    cuboid.mark(grid)

total = 0
for plane in grid:
    for line in plane:
        total += sum(line)

print(total)
