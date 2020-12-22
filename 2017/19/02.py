input = [" " + line[:-1] + " " for line in open("input").readlines()]

input = [" " * len(input[0])] + input + [" " * len(input[0])]

x, y, h = input[1].index("|"), 0, "s"
move = {
    "s": (0, 1),
    "w": (-1, 0),
    "n": (0, -1),
    "e": (1, 0)
}

steps = 0
while True:
    x += move[h][0]
    y += move[h][1]

    if input[y][x] == " ":
        break

    steps += 1

    if input[y][x] == "+":
        if h in "ns":
            if input[y][x - 1] != " ":
                h = "w"
            elif input[y][x + 1] != " ":
                h = "e"
        else:
            if input[y - 1][x] != " ":
                h = "n"
            elif input[y + 1][x] != " ":
                h = "s"

print(steps)
