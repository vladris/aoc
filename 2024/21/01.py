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
    1: { (k1, k2): min(dir_pad_moves[(k1, k2)], key=len) for k1, k2 in dir_pad_moves }
}

def sequence(k1, k2, depth, graph=dir_pad_moves):
    best, best_len = None, 10 ** 10
    for path in graph[(k1, k2)]:
        if len(k := "".join(best_moves[depth][p] for p in zip("A" + path, path))) < best_len:
            best, best_len = k, len(k)
    return best


best_moves[2] = {(k1, k2): sequence(k1, k2, 1, dir_pad_moves) for k1, k2 in dir_pad_moves}
best_moves[3] = {(k1, k2): sequence(k1, k2, 2, num_pad_moves) for k1, k2 in num_pad_moves}

total = 0
for code in codes:
    result = "".join(best_moves[3][pair] for pair in zip("A" + code, code))
    total += len(result) * int(code[:-1])

print(total)
