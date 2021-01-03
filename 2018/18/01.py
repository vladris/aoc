grid = [[c for c in line.strip("\n")] for line in open("input").readlines()]

def adj(x, y):
    counts = { "|": 0, "#": 0, ".": 0 }
    for dx in range(x - 1, x + 2):
        for dy in range(y - 1, y + 2):
            if dx < 0 or dx >= len(grid[0]):
                continue
            if dy < 0 or dy >= len(grid):
                continue
            if dx == x and dy == y:
                continue
            counts[grid[dy][dx]] += 1

    return counts

for _ in range(10):
    new_grid = []
    for y in range(len(grid)):
        new_line = []
        for x in range(len(grid[0])):
            counts = adj(x, y)
            if grid[y][x] == "." and counts["|"] >= 3:
                new_line.append("|")
            elif grid[y][x] == "|" and counts["#"] >= 3:
                new_line.append("#")
            elif grid[y][x] == "#" and counts["#"] >= 1 and counts["|"] >= 1:
                new_line.append("#")
            elif grid[y][x] == "#":
                new_line.append(".")
            else:
                new_line.append(grid[y][x])
        new_grid.append(new_line)
    grid = new_grid

w, l = 0, 0
for line in grid:
    for c in line:
        if c == "|":
            w += 1
        elif c == "#":
            l += 1

print(w * l)
