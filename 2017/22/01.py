input = open("input").readlines()

grid = set()

for y, line in enumerate(input):
    for x, c in enumerate(line.strip()):
        if c == "#":
            grid.add((x, y))

x = len(input[0].strip()) // 2
y = len(input) // 2

mov = [(0, -1), (1, 0), (0, 1), (-1, 0)]

d, bursts = 0, 0

for _ in range(10000):
    if (x, y) in grid:
        d = (d + 1) % 4
        grid.remove((x, y))
    else:
        bursts += 1
        d = (d - 1) % 4
        grid.add((x, y))
    dx, dy = mov[d]
    x += dx
    y += dy

print(bursts)
