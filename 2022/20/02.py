nodes = [(i, v * 811589153) for i, v in enumerate(
    map(int, open('input').read().split('\n')))]


def find(pred):
    for i, n in enumerate(nodes):
        if pred(n):
            return i


for _ in range(10):
    for i in range(len(nodes)):
        idx = find(lambda n: n[0] == i)
        node = nodes.pop(idx)
        idx = (idx + node[1]) % len(nodes)
        nodes.insert(idx, node)


idx = find(lambda n: n[1] == 0)

print(nodes[(idx + 1000) % len(nodes)][1] + nodes[(idx + 2000) %
      len(nodes)][1] + nodes[(idx + 3000) % len(nodes)][1])
