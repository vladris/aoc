input = open("input").readlines()

graph = {}
for line in input:
    node, rest = line.split("<->")
    graph[int(node)] = list(map(int, rest.split(",")))

def visit(node):
    if node in visited:
        return
    
    visited.add(node)
    for n in graph[node]:
        visit(n)

groups = 0
while graph:
    visited = set()
    visit(list(graph.keys())[0])
    groups += 1
    for node in visited:
        graph.pop(node)

print(groups)
