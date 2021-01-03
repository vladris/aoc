import re

input = open("input").readlines()

rs = []
for line in input:
    m = re.match(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line)
    id, x, y = int(m[1]), int(m[2]), int(m[3])
    rs.append((id, x, y, x + int(m[4]), y + int(m[5])))

def intersects(r1, r2):
    return max(r1[1], r2[1]) < min(r1[3], r2[3]) and max(r1[2], r2[2]) < min(r1[4], r2[4])

for r1 in rs:
    i = False
    for r2 in rs:
        if r1 == r2:
            continue
        if intersects(r1, r2):
            i = True
            break
    if not i:
        print(r1[0])
