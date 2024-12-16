grid = [line.strip() for line in open("input").readlines()]

s_i, s_j = len(grid) - 2, 1
e_i, e_j = 1, len(grid[0]) - 2

visited, best, queue = {}, ("E", 10 ** 9), [(s_i, s_j, "E", 0)]
while queue:
    i, j, heading, score = queue.pop(0)
    if grid[i][j] == "#":
        continue

    if (i, j, heading) in visited and visited[(i, j, heading)] <= score:
        continue

    visited[(i, j, heading)] = score

    if i == e_i and j == e_j:
        if score < best[1]:
            best = (heading, score)
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
    

path = set()
def backtrack(i, j, heading, score):
    path.add((i, j))
    
    if i == s_i and j == s_j and heading == "E" and score == 0:
        return
    
    match heading:
        case "E":
            if (i, j, "N") in visited and visited[(i, j, "N")] == score - 1000:
                backtrack(i, j, "N", score - 1000)
            if (i, j, "S") in visited and visited[(i, j, "S")] == score - 1000:
                backtrack(i, j, "S", score - 1000)
            if (i, j - 1, "E") in visited and visited[(i, j - 1, "E")] == score - 1:
                backtrack(i, j - 1, "E", score - 1)
        case "N":
            if (i, j, "W") in visited and visited[(i, j, "W")] == score - 1000:
                backtrack(i, j, "W", score - 1000)
            if (i, j, "E") in visited and visited[(i, j, "E")] == score - 1000:
                backtrack(i, j, "E", score - 1000)
            if (i + 1, j, "N") in visited and visited[(i + 1, j, "N")] == score - 1:
                backtrack(i + 1, j, "N", score - 1)
        case "W":
            if (i, j, "N") in visited and visited[(i, j, "N")] == score - 1000:
                backtrack(i, j, "N", score - 1000)
            if (i, j, "S") in visited and visited[(i, j, "S")] == score - 1000:
                backtrack(i, j, "S", score - 1000)
            if (i, j + 1, "W") in visited and visited[(i, j + 1, "W")] == score - 1:
                backtrack(i, j + 1, "W", score - 1)
        case "S":
            if (i, j, "W") in visited and visited[(i, j, "W")] == score - 1000:
                backtrack(i, j, "W", score - 1000)
            if (i, j, "E") in visited and visited[(i, j, "E")] == score - 1000:
                backtrack(i, j, "E", score - 1000)
            if (i - 1, j, "S") in visited and visited[(i - 1, j, "S")] == score - 1:
                backtrack(i - 1, j, "S", score - 1)


backtrack(e_i, e_j, best[0], best[1])
print(len(path))
