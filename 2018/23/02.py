import re

input = open("input").readlines()

nano = []

for line in input:
    m = re.match(r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)", line)
    nano.append((int(m[1]), int(m[2]), int(m[3]), int(m[4])))

class Vol:
    def __init__(self, x0, x1, y0, y1, z0, z1):
        self.x0, self.x1 = x0, x1
        self.y0, self.y1 = y0, y1
        self.z0, self.z1 = z0, z1

    def point(self):
        return self.x0 == self.x1 and self.y0 == self.y1 and self.z0 == self.z1

    def dist(self):
        return abs(self.x0) + abs(self.y0) + abs(self.z0)

    def inrange(self, n):
        if n[0] < self.x0: dx = self.x0 - n[0]
        elif n[0] > self.x1: dx = n[0] - self.x1
        else: dx = 0

        if n[1] < self.y0: dy = self.y0 - n[1]
        elif n[1] > self.y1: dy = n[1] - self.y1
        else: dy = 0

        if n[2] < self.z0: dz = self.z0 - n[2]
        elif n[2] > self.z1: dz = n[2] - self.z1
        else: dz = 0

        return dx + dy + dz <= n[3]

    def total(self):
        total = 0
        for n in nano:
            if self.inrange(n):
                total += 1
        return total

    def split(self):
        mx = (self.x0 + self.x1) // 2
        my = (self.y0 + self.y1) // 2
        mz = (self.z0 + self.z1) // 2

        yield Vol(self.x0, mx, self.y0, my, self.z0, mz)
        yield Vol(mx + 1, self.x1, self.y0, my, self.z0, mz)
        yield Vol(self.x0, mx, my + 1, self.y1, self.z0, mz)
        yield Vol(mx + 1, self.x1, my + 1, self.y1, self.z0, mz)
        yield Vol(self.x0, mx, self.y0, my, mz + 1, self.z1)
        yield Vol(mx + 1, self.x1, self.y0, my, mz + 1, self.z1)
        yield Vol(self.x0, mx, my + 1, self.y1, mz + 1, self.z1)
        yield Vol(mx + 1, self.x1, my + 1, self.y1, mz + 1, self.z1)

best, pt = 0, Vol(0, 0, 0, 0, 0, 0)

def find(vol):
    global best, pt

    if vol.point():
        if vol.total() > best:
            best = vol.total()
            pt = vol
        elif vol.total() == best:
            if vol.dist() < pt.dist():
                pt = vol
        return
        
    lb, nv = 0, None
    for v in vol.split():
        if v.total() > lb:
            lb = v.total()
            nv = v

    find(nv)

find(Vol(-10 ** 9, 10 ** 9, -10 ** 9, 10 ** 9, -10 ** 9, 10 ** 9))

print(pt.dist())
