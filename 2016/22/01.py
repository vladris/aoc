import re

input = open("input").readlines()[2:]

nodes = {}
for line in input:
    m = re.match(r"/dev/grid/node-x(\d+)-y(\d+)\s*\d+T\s*(\d+)T\s*(\d+)", line)
    nodes[(int(m[1]), int(m[2]))] = (int(m[3]), int(m[4]))

viable = 0
for node in nodes:
    if nodes[node][0] == 0:
        continue

    for node2 in nodes:
        if node2 == node:
            continue

        if nodes[node][0] <= nodes[node2][1]:
            viable += 1

print(viable)
