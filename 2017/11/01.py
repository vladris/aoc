input = open("input").read().strip().split(",")

x, y = 0, 0
for d in input:
    if d == "n":
        y -= 1
    elif d == "ne":
        y -= 1
        x += 1
    elif d == "se":
        x += 1
    elif d == "s":
        y += 1
    elif d == "sw":
        y += 1
        x -= 1
    elif d == "nw":
        x -= 1

print((abs(x) + abs(y) + abs(-(x + y))) // 2)
