grid, moves = open("input").read().split("\n\n")

grid = [list(
    row.replace("#", "##").replace(".", "..").replace("@", "@.").replace("O", "[]")) for row in grid.split("\n")]
moves = "".join(moves.split("\n"))

i, j = len(grid) // 2 - 1, len(grid[0]) // 2 - 2


def can_move(i, j, d):
    if grid[i + d][j] == ".":
        return True
    if grid[i + d][j] == "]":
        return can_move(i + d, j - 1, d) and can_move(i + d, j, d)
    if grid[i + d][j] == "[":
        return can_move(i + d, j, d) and can_move(i + d, j + 1, d)
    return False


def do_move(i, j, d):
    if grid[i][j] == ".":
        return
    elif grid[i][j] == "[":
        do_move(i + d, j, d)
        do_move(i + d, j + 1, d)
        grid[i + d][j], grid[i + d][j + 1] = "[", "]"
        grid[i][j], grid[i][j + 1] = ".", "."
    elif grid[i][j] == "]":
        do_move(i + d, j - 1, d)
        do_move(i + d, j, d)
        grid[i + d][j - 1], grid[i + d][j] = "[", "]"
        grid[i][j - 1], grid[i][j] = ".", "."
    elif grid[i][j] == "@":
        do_move(i + d, j, d)
        grid[i + d][j] = "@"
        grid[i][j] = "."


for move in moves:
    if move == "^" and can_move(i, j, -1):
        do_move(i, j, -1)
        grid[i][j] = "."
        i -= 1
    elif move == "v" and can_move(i, j, 1):
        do_move(i, j, 1)
        grid[i][j] = "."
        i += 1
    elif move == "<":
        t = j - 1
        while grid[i][t] in "[]":
            t -= 1
        if grid[i][t] == ".":
            grid[i].pop(t)
            grid[i].insert(j, ".")
            j -= 1
    elif move == ">":
        t = j + 1
        while grid[i][t] in "[]":
            t += 1
        if grid[i][t] == ".":
            grid[i].pop(t)
            grid[i].insert(j, ".")
            j += 1


gps = 0
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == "[":
            gps += i * 100 + j
print(gps)
