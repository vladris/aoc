grid = [line.strip() for line in open("input").readlines()]
grid = ["#" * (len(grid[0]) + 2)] + ["#" + line + "#" for line in grid] + ["#" * (len(grid[0]) + 2)]

visited = set()

def corners(i, j):
    corners = 0
    if grid[i - 1][j] != grid[i][j] and grid[i][j - 1] != grid[i][j]:
        corners += 1
    elif grid[i - 1][j] == grid[i][j] and grid[i][j - 1] == grid[i][j] and grid[i - 1][j - 1] != grid[i][j]:
        corners += 1

    if grid[i + 1][j] != grid[i][j] and grid[i][j - 1] != grid[i][j]:
        corners += 1
    elif grid[i + 1][j] == grid[i][j] and grid[i][j - 1] == grid[i][j] and grid[i + 1][j - 1] != grid[i][j]:
        corners += 1

    if grid[i - 1][j] != grid[i][j] and grid[i][j + 1] != grid[i][j]:
        corners += 1
    elif grid[i - 1][j] == grid[i][j] and grid[i][j + 1] == grid[i][j] and grid[i - 1][j + 1] != grid[i][j]:
        corners += 1

    if grid[i + 1][j] != grid[i][j] and grid[i][j + 1] != grid[i][j]:
        corners += 1
    elif grid[i + 1][j] == grid[i][j] and grid[i][j + 1] == grid[i][j] and grid[i + 1][j + 1] != grid[i][j]:
        corners += 1

    return corners


def area(i, j):
    if (i, j) in visited:
        return 0, 0

    visited.add((i, j))
    result_a, result_c = 1, corners(i, j)

    if grid[i - 1][j] == grid[i][j]:
        a, c = area(i - 1, j)
        result_a += a
        result_c += c

    if grid[i + 1][j] == grid[i][j]:
        a, c = area(i + 1, j)
        result_a += a
        result_c += c

    if grid[i][j - 1] == grid[i][j]:
        a, c = area(i, j - 1)
        result_a += a
        result_c += c

    if grid[i][j + 1] == grid[i][j]:
        a, c = area(i, j + 1)
        result_a += a
        result_c += c

    return result_a, result_c


total = 0
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        a, c = area(i, j)
        total += a * c

print(total)
