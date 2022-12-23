elves = set()
for y, line in enumerate(open('input').readlines()):
    for x, c in enumerate(line):
        if c == '#':
            elves.add((x, y))

dirs = [((-1, -1), (0, -1), (1, -1)), ((-1, 1), (0, 1), (1, 1)),
        ((-1, -1), (-1, 0), (-1, 1)), ((1, -1), (1, 0), (1, 1))]


def step():
    candidates = {}

    for elf in elves:
        neighbor = False
        for p1, p2, p3 in dirs:
            if elves.intersection({
                    (elf[0] + p1[0], elf[1] + p1[1]),
                    (elf[0] + p2[0], elf[1] + p2[1]),
                    (elf[0] + p3[0], elf[1] + p3[1])}):
                neighbor = True
                continue

            if elf not in candidates:
                candidates[elf] = (elf[0] + p2[0], elf[1] + p2[1])

        if not neighbor or elf not in candidates:
            candidates[elf] = elf

    for elf1 in candidates:
        for elf2 in candidates:
            if elf1 == elf2 or candidates[elf1] != candidates[elf2]:
                continue

            c = candidates[elf1]

            for elf in candidates:
                if candidates[elf] == c:
                    candidates[elf] = elf

    return set(candidates.values())


def area():
    min_x = min(elves, key=lambda elf: elf[0])[0]
    min_y = min(elves, key=lambda elf: elf[1])[1]
    max_x = max(elves, key=lambda elf: elf[0])[0]
    max_y = max(elves, key=lambda elf: elf[1])[1]

    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)


for _ in range(10):
    elves = step()
    dirs = dirs[1:] + [dirs[0]]

print(area())
