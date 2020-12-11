import re

input = open("input").readlines()

aunts = {}
for line in input:
    m = re.match(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", line)
    aunts[m[1]] = {
        (m[2], int(m[3])),
        (m[4], int(m[5])),
        (m[6], int(m[7])),
    }

data = {
    ("children", 3),
    ("cats", 7),
    ("samoyeds", 2),
    ("pomeranians", 3),
    ("akitas", 0),
    ("vizslas", 0),
    ("goldfish", 5),
    ("trees", 3),
    ("cars", 2),
    ("perfumes", 1)
}

for aunt in aunts:
    if not aunts[aunt] - data:
        print(aunt)
