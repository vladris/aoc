elves = set()
for y, line in enumerate(open('input').readlines()):
    for x, c in enumerate(line):
        if c == '#':
            elves.add((x, y))

dirs = [((-1, -1), (0, -1), (1, -1)), ((-1, 1), (0, 1), (1, 1)),
        ((-1, -1), (-1, 0), (-1, 1)), ((1, -1), (1, 0), (1, 1))]


def step():
    candidates = {}
    dest, rem = set(), []

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

        if candidates[elf] in dest:
            rem.append(candidates[elf])
        else:
            dest.add(candidates[elf])

    for to in rem:
        for elf in candidates:
            if candidates[elf] == to:
                candidates[elf] = elf
    return set(candidates.values())


i = 0
while True:
    i += 1
    move = step()
    dirs = dirs[1:] + [dirs[0]]
    if not elves.difference(move):
        break
    elves = move

print(i)
