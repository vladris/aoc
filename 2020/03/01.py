grid = open("input").readlines()

i, trees = 0, 0
for line in grid:
    line = line.strip()
    if line[i] == '#':
        trees += 1

    i = (i + 3) % len(line)

print(trees)