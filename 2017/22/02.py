input = open("input").readlines()

grid = {}

for y, line in enumerate(input):
    for x, c in enumerate(line.strip()):
        if c == "#":
            grid[(x, y)] = "i"

x = len(input[0].strip()) // 2
y = len(input) // 2

mov = [(0, -1), (1, 0), (0, 1), (-1, 0)]

d, bursts = 0, 0

for _ in range(10000000):
    if (x, y) in grid:
        if grid[(x, y)] == "w":
            bursts += 1
            grid[(x, y)] = "i"
        elif grid[(x, y)] == "i":
            d = (d + 1) % 4
            grid[(x, y)] = "f"
        elif grid[(x, y)] == "f":
            d = (d + 2) % 4
            del grid[(x, y)]
    else:
        d = (d - 1) % 4
        grid[(x, y)] = "w"

    dx, dy = mov[d]
    x += dx
    y += dy

print(bursts)
