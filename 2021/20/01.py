with open("input") as f:
    algo = f.readline().strip()
    f.readline()
    grid = [line.strip() for line in f.readlines()]

def pad(grid, c):
    padded = [c * 3 + line + c * 3 for line in grid]
    ln = c * len(padded[0])
    return [ln] * 3 + padded + [ln] * 3

def enhance(grid):
    n = [[None] * len(grid[0]) for _ in range(len(grid))]
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            dot = grid[i - 1][j - 1:j + 2] + grid[i][j - 1:j + 2] + grid[i + 1][j - 1:j + 2]
            idx = int("".join(["0" if c == "." else "1" for c in dot]), base=2)
            n[i][j] = algo[idx]
    return ["".join(line[1:-1]) for line in n[1:-1]], n[1][1]

def lit(grid):
    return sum([sum([1 if c == "#" else 0 for c in line]) for line in grid])

c = "."

for _ in range(2):
    grid, c = enhance(pad(grid, c))

print(lit(grid))
