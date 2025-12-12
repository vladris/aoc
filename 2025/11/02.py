graph = [line.strip().split(" ") for line in open("input").readlines()]
graph = {line[0][:-1]: line[1:] for line in graph}

topological_order = []
visited = set()

def dfs(node):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph.get(node, []):
        dfs(neighbor)
    topological_order.append(node)

for node in graph:
    dfs(node)

topological_order.reverse()

reverse_graph = {}
for node, neighbors in graph.items():
    for neighbor in neighbors:
        reverse_graph.setdefault(neighbor, []).append(node)

def paths(start, end):
    paths = {node: 0 for node in graph}
    paths[start] = 1
    for node in topological_order[topological_order.index(start)+1:topological_order.index(end)+1]:
        paths[node] = sum(paths[prev] for prev in reverse_graph.get(node, []))
    return paths[end]

print(paths("svr", "fft") * paths("fft", "dac") * paths("dac", "out"))
