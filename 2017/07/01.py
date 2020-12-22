input = open("input").readlines()

nodes = {}

for line in input:
    if "->" in line:
        node, children = line.split("->")
        children = list(map(str.strip, children.split(",")))
    else:
        node, children = line, []
    name, value = node.split("(")
    name, value = name.strip(), int(value.strip()[:-1])
    nodes[name] = (value, children)

for node in nodes:
    root = True
    for n in nodes:
        if node in nodes[n][1]:
            root = False
            break
    if root:
        break

print(node)
