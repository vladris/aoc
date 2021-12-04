cmds = open("input").readlines()

h, d, a = 0, 0, 0
for cmd in cmds:
    match cmd.split():
        case ["down", i]: a += int(i)
        case ["up", i]: a -= int(i)
        case ["forward", i]:
            h += int(i)
            d += a * int(i)

print(h * d)
