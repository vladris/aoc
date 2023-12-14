grids = [grid.strip().split('\n') for grid in open('input').read().split('\n\n')]

def col_reflection(grid):
    for col in range(len(grid[0]) - 1):
        i, j = col, col + 1
        while i >= 0 and j < len(grid[0]) and all(
            [line[i] == line[j] for line in grid]):
            i -= 1
            j += 1

        if i == -1 or j == len(grid[0]):
            return col + 1


def row_reflection(grid):
    for row in range(len(grid) - 1):
        i, j = row, row + 1
        while i >= 0 and j < len(grid) and grid[i] == grid[j]:
            i -= 1
            j += 1

        if i == -1 or j == len(grid):
            return row + 1


def reflection(grid):
    if reflection := col_reflection(grid):
        return reflection
    else:
        return row_reflection(grid) * 100


print(sum([reflection(grid) for grid in grids]))
