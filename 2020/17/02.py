input = open("input").readlines()

state = set()
for i, line in enumerate(input):
    for j, c in enumerate(line):
        if c == '#':
            state.add((i, j, 0, 0))

def neighbors(x, y, z, w):
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if i == j == k == l == 0:
                        continue
                    yield x + i, y + j, z + k, w + l

def active(x, y, z, w):
    total = 0
    for i, j, k, l in neighbors(x, y, z, w):
        if (i, j, k, l) in state:
            total += 1
    return total

def step():
    global state
    newstate = set()

    for x, y, z, w in state:
        if 2 <= active(x, y, z, w) <= 3:
            newstate.add((x, y, z, w))

        for nx, ny, nz, nw in neighbors(x, y, z, w):
            if (nx, ny, nz, nw) not in state and active(nx, ny, nz, nw) == 3:
                newstate.add((nx, ny, nz, nw))
    state = newstate

for _ in range(6):
    step()

print(len(state))