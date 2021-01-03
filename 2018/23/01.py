import re

input = open("input").readlines()

nano, best = [], (0, 0, 0, 0)

for line in input:
    m = re.match(r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)", line)
    nano.append((int(m[1]), int(m[2]), int(m[3]), int(m[4])))
    if nano[-1][3] > best[3]:
        best = nano[-1]

print(sum([abs(n[0] - best[0]) + abs(n[1] - best[1]) + abs(n[2] - best[2]) <= best[3] for n in nano]))
