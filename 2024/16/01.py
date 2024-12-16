grid = [line.strip() for line in open("input").readlines()]

s_i, s_j = len(grid) - 2, 1
e_i, e_j = 1, len(grid[0]) - 2

visited, best, queue = {}, 10 ** 9, [(s_i, s_j, "E", 0)]
while queue:
    i, j, heading, score = queue.pop(0)
    if grid[i][j] == "#":
        continue

    if (i, j, heading) in visited and visited[(i, j, heading)] <= score:
        continue

    visited[(i, j, heading)] = score

    if i == e_i and j == e_j:
        if score < best:
            best = score
        continue

    match heading:
        case "E":
            queue.append((i, j, "N", score + 1000))
            queue.append((i, j, "S", score + 1000))
            queue.append((i, j + 1, heading, score + 1))
        case "N":
            queue.append((i, j, "W", score + 1000))
            queue.append((i, j, "E", score + 1000))
            queue.append((i - 1, j, heading, score + 1))
        case "W":
            queue.append((i, j, "N", score + 1000))
            queue.append((i, j, "S", score + 1000))
            queue.append((i, j - 1, heading, score + 1))
        case "S":
            queue.append((i, j, "W", score + 1000))
            queue.append((i, j, "E", score + 1000))
            queue.append((i + 1, j, heading, score + 1))
    
print(best)
