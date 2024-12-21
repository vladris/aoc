codes = [line.strip() for line in open("input").readlines()]

num_pad = {
    "A": { "<": "0", "^": "3" },
    "0": { ">": "A", "^": "2" },
    "1": { "^": "4", ">": "2"},
    "2": { "<": "1", "^": "5", ">": "3", "v": "0" },
    "3": { "<": "2", "^": "6", "v": "A" },
    "4": { "^": "7", ">": "5", "v": "1" },
    "5": { "<": "4", "^": "8", ">": "6", "v": "2" },
    "6": { "<": "5", "^": "9", "v": "3" },
    "7": { ">": "8", "v": "4" },
    "8": { "<": "7", ">": "9", "v": "5" },
    "9": { "<": "8", "v": "6" },
}

dir_pad = {
    "^": { ">": "A", "v": "v" },
    "A": { "<": "^", "v": ">" },
    "<": { ">": "v" },
    "v": { "<": "<", "^": "^", ">": ">" },
    ">": { "<": "v", "^": "A" }
}

def paths(i, dest, result, graph, visited, path):
    if i == dest:
        result.append("".join(path) + "A")
        return

    visited.add(i)

    for direction, next_i in graph[i].items():
        if next_i in visited:
            continue
        
        visited.add(next_i)
        path.append(direction)
        
        paths(next_i, dest, result, graph, visited, path)
        
        visited.remove(next_i)
        path.pop()


def map_path(graph):
    path_map = {}
    for k1 in graph:
        for k2 in graph:
            if k1 == k2:
                path_map[(k1, k2)] = ["A"]
                continue

            result = []
            paths(k1, k2, result, graph, set(), [])
            path_map[(k1, k2)] = result
    return path_map


num_pad_moves = map_path(num_pad)
dir_pad_moves = map_path(dir_pad)

best_moves = {
    1: { (k1, k2): len(min(dir_pad_moves[(k1, k2)], key=len)) for k1, k2 in dir_pad_moves }
}

def sequence(k1, k2, depth, graph=dir_pad_moves):
    best = 10 ** 20
    for path in graph[(k1, k2)]:
        if (k := sum(best_moves[depth][p] for p in zip("A" + path, path))) < best:
            best = k
    return best


for i in range(2, 26):
    best_moves[i] = {(k1, k2): sequence(k1, k2, i - 1, dir_pad_moves) for k1, k2 in dir_pad_moves}
best_moves[26] = {(k1, k2): sequence(k1, k2, 25, num_pad_moves) for k1, k2 in num_pad_moves}

total = 0
for code in codes:
    result = sum(best_moves[26][pair] for pair in zip("A" + code, code))
    total += result * int(code[:-1])

print(total)
