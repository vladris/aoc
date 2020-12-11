moves = open("input").read()

x1, y1, x2, y2, visited = 0, 0, 0, 0, set()

def move(x, y, c):
    if c == '<': x -= 1
    if c == '>': x += 1
    if c == 'v': y -= 1
    if c == '^': y += 1
    return x, y

for i in range(len(moves)):
    if i % 2:
        x1, y1 = move(x1, y1, moves[i])
        visited.add((x1, y1))
    else:
        x2, y2 = move(x2, y2, moves[i])
        visited.add((x2, y2))

print(len(visited))