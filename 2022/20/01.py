nodes = [(i, v) for i, v in enumerate(
    map(int, open('input').read().split('\n')))]

initial = nodes[:]

for node in initial:
    idx = nodes.index(node)
    node = nodes.pop(idx)
    idx = (idx + node[1]) % len(nodes)
    nodes.insert(idx, node[1])

idx = nodes.index(0)
print(nodes[(idx + 1000) % len(nodes)] + nodes[(idx + 2000) %
      len(nodes)] + nodes[(idx + 3000) % len(nodes)])
