lines = open("input").readlines()

edges = {}
for line in lines:
    a, b = line.strip().split("-")
    if not a in edges:
        edges[a] = []
    if not b in edges:
        edges[b] = []
    edges[a].append(b)
    edges[b].append(a)

total = 0

def paths(node, visited):
    global total

    if node == "end":
        total += 1
        return

    if node.islower() and node in visited:
        return

    visited.append(node)

    for n in edges[node]:
        paths(n, visited[:])

paths("start", [])

print(total)
