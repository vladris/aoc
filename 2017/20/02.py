import re

input = open("input").readlines()

class Particle:
    def __init__(self, id, px, py, pz, vx, vy, vz, ax, ay, az):
        self.id = id
        self.p = (int(px), int(py), int(pz))
        self.v = (int(vx), int(vy), int(vz))
        self.a = (int(ax), int(ay), int(az))

    def dist(self):
        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])

    def step(self):
        self.v = (self.v[0] + self.a[0], self.v[1] + self.a[1], self.v[2] + self.a[2])
        self.p = (self.p[0] + self.v[0], self.p[1] + self.v[1], self.p[2] + self.v[2])

    def __str__(self):
        return f"{self.p}, {self.v}, {self.a}"

particles = []
for i, line in enumerate(input):
    m = re.match(r"p=<(.*),(.*),(.*)>, v=<(.*),(.*),(.*)>, a=<(.*),(.*),(.*)>", line)
    particles.append(Particle(i, *m.groups()))


for _ in range(1000):
    pos = {}
    for p in particles:
        p.step()
        if p.p not in pos:
            pos[p.p] = []
        pos[p.p].append(p)

    for k in pos:
        if len(pos[k]) > 1:
            for p in pos[k]:
                particles.remove(p)

print(len(particles))
