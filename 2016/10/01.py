import re

input = open("input").readlines()

rules = {}
values = {}

for line in input:
    m = re.match(r"bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)", line)
    if m:
        l = int(m[3]) if m[2] == "bot" else -1
        h = int(m[5]) if m[4] == "bot" else -1
        rules[int(m[1])] = (l, h)
        if l != -1 and l not in values:
            values[l] = []
        if h != -1 and h not in values:
            values[h] = []
        continue

    m = re.match(r"value (\d+) goes to bot (\d+)", line)
    v, b = int(m[1]), int(m[2])
    if b not in values:
        values[b] = []
    values[b].append(v)

while True:
    for b in values:
        if len(values[b]) == 2:
            l, h = min(values[b]), max(values[b])
            if l == 17 and h == 61:
                print(b)
                exit()

            values[b] = []
            if rules[b][0] != -1:
                values[rules[b][0]].append(l)
            if rules[b][1] != -1:
                values[rules[b][1]].append(h)
