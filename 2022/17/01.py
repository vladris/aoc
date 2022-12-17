jets = open('input').read()

rocks = [{(0, 0), (1, 0), (2, 0), (3, 0)}, 
         {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)},
         {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)},
         {(0, 0), (0, 1), (0, 2), (0, 3)},
         {(0, 0), (0, 1), (1, 0), (1, 1)}]

grid = set({(i, 0) for i in range(1, 8)})


def intersects(rock, grid):
    for block in rock:
        if block in grid or block[0] <= 0 or block[0] >= 8:
            return True
    return False


def move(rock, dx, dy):
    return {(i + dx, j + dy) for i, j in rock}


rock_i, jet_i = 0, 0
for _ in range(2022):
    top = max(grid, key=lambda pt: pt[1])[1]
    rock = move(rocks[rock_i], 3, top + 4)

    while True:
        new_pos = move(rock, 1 if jets[jet_i] == '>' else -1, 0)
        jet_i += 1
        if jet_i == len(jets):
            jet_i = 0
        if not intersects(new_pos, grid):
            rock = new_pos
        new_pos = move(rock, 0, -1)
        if intersects(new_pos, grid):
            break
        rock = new_pos

    grid |= rock
    rock_i += 1
    if rock_i == len(rocks):
        rock_i = 0

print(max(grid, key=lambda pt: pt[1])[1])
