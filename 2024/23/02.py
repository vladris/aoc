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

def all_connected(group):
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            if group[i] not in graph[group[j]]:
                return False
    return True


best = []
for k in graph:
    subsets = [combo for r in range(len(best), len(graph[k]) + 1) for combo in itertools.combinations(graph[k], r)]
    for subset in subsets:
        if all_connected([k] + list(subset)):
            best = [k] + list(subset)

print(",".join(sorted(best)))
