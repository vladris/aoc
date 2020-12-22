input = open("input").read().split(",")

dancers = [chr(ord("a") + i) for i in range(16)]

for line in input:
    c, line = line[0], line[1:]
    if c == "s":
        s = int(line)
        dancers = dancers[-s:] + dancers[:-s]
    elif c == "x":
        p1, p2 = map(int, line.split("/"))
        dancers[p1], dancers[p2] = dancers[p2], dancers[p1]
    elif c == "p":
        d1, d2 = line.split("/")
        p1, p2 = dancers.index(d1), dancers.index(d2)
        dancers[p1], dancers[p2] = dancers[p2], dancers[p1]

print("".join(dancers))
