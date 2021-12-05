class Point:
    def __init__(self, s):
        self.x, self.y = map(int, s.split(","))

class Line:
    def __init__(self, s):
        self.p1, self.p2 = map(Point, s.split(" -> "))

lines = map(Line, open("input").readlines())

grid = [[0] * 1000 for _ in range(1000)]

for line in lines:
    x, y = line.p1.x, line.p1.y
    dx = -1 if line.p1.x > line.p2.x else 1 if line.p1.x < line.p2.x else 0
    dy = -1 if line.p1.y > line.p2.y else 1 if line.p1.y < line.p2.y else 0

    while x != line.p2.x or y != line.p2.y:
        grid[y][x] += 1
        x += dx
        y += dy

    grid[y][x] +=1

print(sum([sum([int(pt > 1) for pt in row]) for row in grid]))
