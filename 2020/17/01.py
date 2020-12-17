input = open("input").readlines()

state = set()
for i, line in enumerate(input):
    for j, c in enumerate(line):
        if c == '#':
            state.add((i, j, 0))

def neighbors(x, y, z):
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if i == j == k == 0:
                    continue
                yield x + i, y + j, z + k

def active(x, y, z):
    total = 0
    for i, j, k in neighbors(x, y, z):
        if (i, j, k) in state:
            total += 1
    return total

def step():
    global state
    newstate = set()

    for x, y, z in state:
        if 2 <= active(x, y, z) <= 3:
            newstate.add((x, y, z))

        for nx, ny, nz in neighbors(x, y, z):
            if (nx, ny, nz) not in state and active(nx, ny, nz) == 3:
                newstate.add((nx, ny, nz))
    state = newstate

for _ in range(6):
    step()

print(len(state))