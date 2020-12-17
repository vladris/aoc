import re

intervals = []

with open("input") as f:
    while True:
        m = re.match(r".*: (\d+)-(\d+) or (\d+)-(\d+)", f.readline())
        if not m:
            break
        intervals += [(int(m[1]), int(m[2])), (int(m[3]), int(m[4]))]

    for _ in range(4):
        f.readline()

    error = 0
    for line in f.readlines():
        for num in list(map(int, line.split(","))):
            if not any(map(lambda x: x[0] <= num and num <= x[1], intervals)):
                error += num

print(error)
