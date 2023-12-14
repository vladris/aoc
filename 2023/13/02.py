grids = [grid.strip().split('\n') for grid in open('input').read().split('\n\n')]

def col_reflection(grid):
    for col in range(len(grid[0]) - 1):
        i, j = col, col + 1
        while i >= 0 and j < len(grid[0]) and all(
            [line[i] == line[j] for line in grid]):
            i -= 1
            j += 1

        if i == -1 or j == len(grid[0]):
            yield col + 1


def row_reflection(grid):
    for row in range(len(grid) - 1):
        i, j = row, row + 1
        while i >= 0 and j < len(grid) and grid[i] == grid[j]:
            i -= 1
            j += 1

        if i == -1 or j == len(grid):
            yield row + 1


def reflection(grid):
    for reflection in col_reflection(grid):
        yield reflection

    for reflection in row_reflection(grid):
        yield reflection * 100


def new_reflection(grid):
    original = next(reflection(grid))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            new_grid = grid[:]
            
            if grid[i][j] == '.':
                new_grid[i] = new_grid[i][:j] + '#' + new_grid[i][j + 1:]
            else:
                new_grid[i] = new_grid[i][:j] + '.' + new_grid[i][j + 1:]

            for refl in reflection(new_grid):
                if refl != original:
                    return refl


print(sum([new_reflection(grid) for grid in grids]))
