class Point:
    def __init__(self, s):
        self.x, self.y = map(int, s.split(","))

class Line:
    def __init__(self, s):
        self.p1, self.p2 = map(Point, s.split(" -> "))

lines = map(Line, open("input").readlines())

grid = [[0] * 1000 for _ in range(1000)]

for line in lines:
    if line.p1.y == line.p2.y:
        for x in range(min(line.p1.x, line.p2.x), max(line.p1.x, line.p2.x) + 1):
            grid[line.p1.y][x] += 1

    if line.p1.x == line.p2.x:
        for y in range(min(line.p1.y, line.p2.y), max(line.p1.y, line.p2.y) + 1):
            grid[y][line.p1.x] += 1

print(sum([sum([int(pt > 1) for pt in row]) for row in grid]))
