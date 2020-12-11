moves = open("input").read()

x, y, visited = 0, 0, set()
for c in moves:
    if c == '<': x -= 1
    if c == '>': x += 1
    if c == 'v': y -= 1
    if c == '^': y += 1
    visited.add((x, y))

print(len(visited))