from functools import reduce
import operator

grid = open("input").readlines()

def slope(i, j):
    x, y, trees = 0, 0, 0
    while y < len(grid):
        line = grid[y].strip()
        if line[x] == '#':
            trees += 1

        x = (x + i) % len(line)
        y += j
    return trees

print(reduce(operator.mul, map(lambda ij: slope(*ij), [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)])))