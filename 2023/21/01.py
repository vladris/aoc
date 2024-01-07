grid = [line.strip() for line in open('input').readlines()]

tiles = set()
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            tiles.add((i, j))
            break
    else:
        continue
    break

for _ in range(64):
    new_tiles = set()
    for tile in tiles:
        x, y = tile

        if x > 0 and grid[x - 1][y] != '#':
            new_tiles.add((x - 1, y))
        if x < len(grid) - 1 and grid[x + 1][y] != '#':
            new_tiles.add((x + 1, y))
        if y > 0 and grid[x][y - 1] != '#':
            new_tiles.add((x, y - 1))
        if y < len(grid[0]) - 1 and grid[x][y + 1] != '#':
            new_tiles.add((x, y + 1))

    tiles = new_tiles

print(len(new_tiles))
