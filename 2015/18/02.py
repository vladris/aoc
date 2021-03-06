grid = [["."] * 102] + [list("." + x[:-1] + ".") for x in open("input").readlines()] + [["."] * 102]

def step():
    new = [["." for _ in range(102)] for _ in range(102)]

    grid[1][1] = "#"
    grid[1][100] = "#"
    grid[100][1] = "#"
    grid[100][100] = "#"

    for i in range(1, 101):
        for j in range(1, 101):
            on = ((grid[i - 1][j - 1] == "#") +
                (grid[i - 1][j] == "#") +
                (grid[i - 1][j + 1] == "#") +
                (grid[i][j - 1] == "#") +
                (grid[i][j + 1] == "#") +
                (grid[i + 1][j - 1] == "#") +
                (grid[i + 1][j] == "#") +
                (grid[i + 1][j + 1] == "#"))

            if grid[i][j] == "#":
                new[i][j] = "#" if on == 2 or on == 3 else "."
            else:
                new[i][j] = "#" if on == 3 else "."

    new[1][1] = "#"
    new[1][100] = "#"
    new[100][1] = "#"
    new[100][100] = "#"
    return new

for i in range(100):
    grid = step()

total = 0
for i in range(1, 101):
    for j in range(1, 101):
        total += grid[i][j] == "#"
print(total)