lines = [line.split() for line in open("input").readlines()]
lines = [list(map(int, l)) for l in lines]

total = 0
for line in lines:
    direction = 1 if line[0] > line[1] else -1
    total += all([1 <= (x - y) * direction <= 3 for x, y in zip(line, line[1:])])

print(total)
