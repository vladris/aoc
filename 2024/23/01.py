import itertools

pairs = [line.strip().split("-") for line in open("input").readlines()]

graph = {}
for pair in pairs:
    if pair[0] not in graph:
        graph[pair[0]] = set()
    graph[pair[0]].add(pair[1])

    if pair[1] not in graph:
        graph[pair[1]] = set()
    graph[pair[1]].add(pair[0])

total = 0
for group in itertools.combinations(graph.keys(), 3):
    if group[0][0] != "t" and group[1][0] != "t" and group[2][0] != "t":
        continue
    if group[1] in graph[group[0]] and group[2] in graph[group[0]] and group[2] in graph[group[1]]:
        total += 1

print(total)
