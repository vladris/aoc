seats = open("input").readlines()

seats = list(map(lambda s: list("L" + s.strip() + "L"), seats))

h, w = len(seats), len(seats[0]) - 2

seats = ["L" * (w + 2)] + seats + ["L" * (w + 2)]

def step(seats):
    same, new = True, [[c for c in line] for line in seats]
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            occ = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    dx, dy = i + x, j + y
                    while seats[dx][dy] == ".":
                        dx += x
                        dy += y

                    if seats[dx][dy] == "#":
                        occ += 1

            if seats[i][j] == "L" and occ == 0:
                same = False
                new[i][j] = "#"
            elif seats[i][j] == "#" and occ >= 5:
                same = False
                new[i][j] = "L"

    return same, new

same = False
while not same:
    same, seats = step(seats)

print(sum([sum([c == '#' for c in line]) for line in seats]))
