input = open("input").read().strip().split("\n\n")

tiles = {}
for tile in input:
    id, rest = tile.split("\n", 1)
    id = int(id[5:-1])
    grid = rest.split("\n") 
    borders = ["", "", "", ""]
    for i in range(len(grid)):
        borders[0] += grid[0][i]
        borders[1] += grid[i][-1]
        borders[2] += grid[len(grid) - 1][i]
        borders[3] += grid[i][0]
    tiles[id] = borders + [b[::-1] for b in borders]

corners = 1
for tile in tiles:
    matches = 0
    for border in tiles[tile]:
        for tile2 in tiles:
            if tile == tile2:
                continue
            if border in tiles[tile2]:
                matches += 1
                break
    if matches // 2 == 2:
        corners *= tile

print(corners)
