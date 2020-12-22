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

def weight(n):
    if not nodes[n][1]:
        return nodes[n][0]

    w = set([weight(child) for child in nodes[n][1]])

    if len(w) == 1:
        return nodes[n][0] + w.pop() * len(nodes[n][1])

    ws = {}
    for child in nodes[n][1]:
        cw = weight(child)
        if cw not in ws:
            ws[cw] = []
        ws[cw] += [child]

    for cw in ws:
        if len(ws[cw]) == 1:
            delta = cw - (w - {cw}).pop()
            print(nodes[ws[cw][0]][0] - delta)
            exit()

weight("veboyvy")
