graph = [line.strip().split(':') for line in open('input').readlines()]
graph = {l[0]: {i for i in l[1].strip().split(' ')} for l in graph}

for k in dict(graph):
    for v in graph[k]:
        if v not in graph:
            graph[v] = set()
        graph[v].add(k)


def most_connected(n, visited):
    best_n, best_d = None, 0
    for n in graph:
        if n in visited:
            continue

        neighbors = sum(1 for v in graph[n] if v in visited)
        if neighbors > best_d:
            best_n, best_d = n, neighbors

    return best_n



def find_components():
    start = list(graph.keys())[0]
    visited = {start}
    while len(visited) < len(graph):
        total = 0
        for n in visited:
            total += sum(1 for v in graph[n] if v not in visited)
        
        if total == 3:
            return visited

        n = most_connected(start, visited)
        visited.add(n)


l = len(find_components())
print(l * (len(graph) - l))
