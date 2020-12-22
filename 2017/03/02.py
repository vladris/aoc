input = 312051

grid = {(0, 0): 1}

def get(x, y):
    return 0 if (x, y) not in grid else grid[(x, y)]

x, y, d, c, cd = 0, 0, 1, 2, 1

value = 0
while True:
    if cd == 0:
        c -= 1
        if c == 0:
            c = 2
            d += 1
        cd = d
    cd -= 1

    if d % 2 == 1:
        if c == 2:
            x += 1
        else:
            y -= 1
    else:
        if c == 2:
            x -= 1
        else:
            y += 1

    value = get(x - 1, y - 1) + get(x, y - 1) + get(x + 1, y - 1) + get(x - 1, y) + get(x + 1, y) + get(x - 1, y + 1) + get(x, y + 1) + get(x + 1, y + 1)

    if value > input:
        break

    grid[(x, y)] = value

print(value)
