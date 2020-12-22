input = open("input").readlines()

graph = {}
for line in input:
    node, rest = line.split("<->")
    graph[int(node)] = list(map(int, rest.split(",")))

visited = set()
def visit(node):
    if node in visited:
        return
    
    visited.add(node)
    for n in graph[node]:
        visit(n)

visit(0)
print(len(visited))
