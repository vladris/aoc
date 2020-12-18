lines = open("input").readlines()

pad = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
x, y = 1, 1

for line in lines:
    for c in line:
        if c == "U" and y > 0: y -= 1
        if c == "D" and y < 2: y += 1
        if c == "L" and x > 0: x -= 1
        if c == "R" and x < 2: x += 1
    print(pad[y][x], end="")
