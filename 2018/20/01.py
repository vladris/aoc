input = [c for c in open("input").read().strip()]

rooms = {(0, 0): set()}

def regex(r, i, x, y):
    while True:
        if r[i] == "(":
            while r[i] != ")":
                i = regex(r, i + 1, x, y)
            i += 1
            continue

        if r[i] in "$|)":
            return i

        rooms[(x, y)].add(r[i])
        opp = ""
        if r[i] == "N":
            y -= 1
            opp = "S"
        if r[i] == "E":
            x += 1
            opp = "W"
        if r[i] == "S":
            y += 1
            opp = "N"
        if r[i] == "W":
            x -= 1
            opp = "E"

        if (x, y) not in rooms:
            rooms[(x, y)] = set()
        rooms[(x, y)].add(opp)

        i += 1

regex(input, 1, 0, 0)

distances = {}
queue = [(0, 0, 0)]

while queue:
    x, y, d = queue.pop(0)
    if (x, y) in distances and distances[(x, y)] <= d:
        continue
    else:
        distances[(x, y)] = d

    if "N" in rooms[(x, y)]: queue.append((x, y - 1, d + 1))
    if "E" in rooms[(x, y)]: queue.append((x + 1, y, d + 1))
    if "S" in rooms[(x, y)]: queue.append((x, y + 1, d + 1))
    if "W" in rooms[(x, y)]: queue.append((x - 1, y, d + 1))
    
print(max(distances.values()))
