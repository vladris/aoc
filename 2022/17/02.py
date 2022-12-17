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


def top():
    return max(grid, key=lambda pt: pt[1])[1]

rock_i, jet_i = 0, 0
cache, delta_top = {}, 0
i = 0
while i < 10_000:
    rock = move(rocks[rock_i], 3, top() + 4)

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

    i += 1
    
    if not delta_top:
        if (rock_i, jet_i) not in cache:
            cache[(rock_i, jet_i)] = []
        c = cache[(rock_i, jet_i)]
        c.append([i, top()])
        if len(c) > 2 and c[-1][1] - c[-2][1] == c[-2][1] - c[-3][1]:
            period, growth = c[-1][0] - c[-2][0], c[-1][1] - c[-2][1]
            delta_top = (1_000_000_000_000 - i) // period * growth
            i = 10_000 - (1_000_000_000_000 - i) % period

print(top() + delta_top)
 