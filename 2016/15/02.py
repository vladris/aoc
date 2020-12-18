import re

input = open("input").readlines()

discs = []

for line in input:
    m = re.match(".* (\d+) positions; .*position (\d+)", line)
    discs.append((int(m[1]), int(m[2])))

discs.append((11, 0))

t = 0
while True:
    bounce = False
    for i, d in enumerate(discs):
        if (d[1] + t + i + 1) % d[0] != 0:
            bounce = True
            break

    if not bounce:
        break
    t += 1

print(t)
