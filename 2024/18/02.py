bytes = [tuple(map(int, line.strip().split(","))) for line in open("input").readlines()]

def reachable(memory):
    visited, queue = set(), [(0, 0)]
    while queue:
        i, j = queue.pop(0)
        if i == 70 and j == 70:
            return True

        if i < 0 or j < 0 or i > 70 or j > 70:
            continue

        if (i, j) in memory:
            continue

        if (i, j) in visited:
            continue
        else:
            visited.add((i, j))

        queue.append((i + 1, j))
        queue.append((i - 1, j))
        queue.append((i, j + 1))
        queue.append((i, j - 1))
    return False


i = 1024
memory = set(bytes[:i])

while reachable(memory):
    memory.add(bytes[i])
    i += 1

print(f"{bytes[i - 1][0]},{bytes[i - 1][1]}")
