class Cuboid:
    def __init__(self, x, y, z):
        self.x0, self.x1 = x[0], x[1]
        self.y0, self.y1 = y[0], y[1]
        self.z0, self.z1 = z[0], z[1]

    def intersect(self, c):
        result = Cuboid(
            (max(self.x0, c.x0), min(self.x1, c.x1)),
            (max(self.y0, c.y0), min(self.y1, c.y1)),
            (max(self.z0, c.z0), min(self.z1, c.z1)))

        if result.x0 <= result.x1 and result.y0 <= result.y1 and result.z0 <= result.z1:
            return result

    def volume(self):
        return (self.x1 - self.x0 + 1) * (self.y1 - self.y0 + 1) * (self.z1 - self.z0 + 1)

def coord(s):
    return tuple(map(int, s[2:].split("..")))

cuboids = []
for line in open("input").readlines():
    c = line[3:].strip().split(",")
    cuboids.append((line.startswith("on"), Cuboid(coord(c[0]), coord(c[1]), coord(c[2]))))

inc, exc = [], []
for on, cuboid in cuboids:
    i = filter(None, [c.intersect(cuboid) for c in exc])
    e = filter(None, [c.intersect(cuboid) for c in inc])
    inc += i
    exc += e

    if on:
        inc.append(cuboid)

total = sum(c.volume() for c in inc) - sum(c.volume() for c in exc)
print(total)
