import re

input = open("input").readlines()

aunts = {}
for line in input:
    m = re.match(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", line)
    aunts[m[1]] = {
        m[2]: int(m[3]),
        m[4]: int(m[5]),
        m[6]: int(m[7]),
    }

data = {
    "children": lambda x: x == 3,
    "cats": lambda x: x > 7,
    "samoyeds": lambda x: x == 2,
    "pomeranians": lambda x: x < 3,
    "akitas": lambda x: x == 0,
    "vizslas": lambda x: x == 0,
    "goldfish": lambda x: x < 5,
    "trees": lambda x: x > 3,
    "cars": lambda x: x == 2,
    "perfumes": lambda x: x == 1
}

for aunt in aunts:
    if sum([data[k](aunts[aunt][k]) for k in aunts[aunt]]) == 3:
        print(aunt)
