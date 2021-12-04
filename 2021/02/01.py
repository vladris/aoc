cmds = open("input").readlines()

h, d = 0, 0
for cmd in cmds:
    match cmd.split():
        case ["down", i]: d += int(i)
        case ["up", i]: d -= int(i)
        case ["forward", i]: h += int(i)

print(h * d)