import re

input = open("input").readlines()[2:]

nodes = {}
for line in input:
    m = re.match(r"/dev/grid/node-x(\d+)-y(\d+)\s*\d+T\s*(\d+)T\s*(\d+)", line)
    nodes[(int(m[1]), int(m[2]))] = (int(m[3]), int(m[4]))

def render():
    for y in range(35):
        for x in range(30):
            if x == y == 0:
                print("0", end="")
            elif x == 4 and y == 25:
                print("_", end="")
            elif x == 29 and y == 0:
                print("G", end="")
            elif nodes[(x, y)][0] > 400:
                print("#", end="")
            else:
                print(".", end="")
        print()

goal = (max(nodes.keys(), key=lambda k: k[0])[0], 0)
empty = min(nodes.keys(), key=lambda k: nodes[k][0])

total = empty[0] + empty[1] + goal[0] + 5 * (goal[0] - 1)
print(total)
