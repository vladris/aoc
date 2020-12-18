lines = open("input").readlines()

pad = [(0, 0, 1, 0, 0), (0, 2, 3, 4, 0), (5, 6, 7, 8, 9), (0, 10, 11, 12, 0), (0, 0, 13, 0, 0)]
x, y = 2, 2

for line in lines:
    for c in line:
        if c == "U" and y > 0 and pad[y - 1][x]: y -= 1
        if c == "D" and y < 4 and pad[y + 1][x]: y += 1
        if c == "L" and x > 0 and pad[y][x - 1]: x -= 1
        if c == "R" and x < 4 and pad[y][x + 1]: x += 1
    print("{:X}".format(pad[y][x]), end="")
