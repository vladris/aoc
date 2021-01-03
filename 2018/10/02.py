import re

class Star:
    def __init__(self, x, y, vx, vy):
        self.x, self.y, self.vx, self.vy = x, y, vx, vy
    
    def step(self, steps=1):
        self.x += self.vx * steps
        self.y += self.vy * steps

def dist(s1, s2):
    return abs(s1.x - s2.x) + abs(s1.y - s2.y)

stars = []

for line in open("input").readlines():
    m = re.match(r".*<(.+), (.+)>.*<(.+), (.+)>", line)
    stars.append(Star(int(m[1]), int(m[2]), int(m[3]), int(m[4])))

steps = 0
while dist(stars[0], stars[1]) > 10:
    stars[0].step()
    stars[1].step()
    steps += 1

for star in stars[2:]:
    star.step(steps)

def show():
    minx, miny, maxx, maxy = 10 ** 6, 10 ** 6, 0, 0
    for star in stars:
        if star.x < minx: minx = star.x
        if star.y < miny: miny = star.y
        if star.x > maxx: maxx = star.x
        if star.y > maxy: maxy = star.y

    grid = [["." for _ in range(maxx - minx + 1)] for _ in range(maxy - miny + 1)]
    for star in stars:
        grid[star.y - miny][star.x - minx] = "#"

    for line in grid:
        print("".join(line))

while True:
    print(f"Steps: {steps}")
    show()
    input()
    for star in stars:
        star.step()
    steps += 1
