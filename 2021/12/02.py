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

def valid(node, visited):
    if node.isupper():
        return True

    if node == "start" and visited:
        return False
    
    if len(set(visited)) == len(visited):
        return True

    return node not in visited


def paths(node, visited):
    global total

    if node == "end":
        total += 1
        return

    if not valid(node, visited):
        return

    if node.islower():
        visited.append(node)

    for n in edges[node]:
        paths(n, visited[:])

paths("start", [])
print(total)
