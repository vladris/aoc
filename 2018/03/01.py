import re

input = open("input").readlines()

rs = []
for line in input:
    m = re.match(r".*@ (\d+),(\d+): (\d+)x(\d+)", line)
    rs.append((int(m[1]), int(m[2]), int(m[3]), int(m[4])))

def fill(r):
    for x in range(r[2]):
        for y in range(r[3]):
            yield r[0] + x, r[1] + y

areas, claims = set(), set()
for r in rs:
    area = set(fill(r))
    claims = claims.union(areas.intersection(area))
    areas = areas.union(area)

print(len(claims))
