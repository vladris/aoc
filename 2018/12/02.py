input = open("input").readlines()

state = input[0][15:].strip()
rules = {}

for line in input[2:]:
    p, r = line.strip().split(" => ")
    rules[p] = r

l = 0

for c in range(1000):
    nstat = ""
    state = "...." + state + "...."
    for i in range(len(state) - 4):
        nstat += rules[state[i:i + 5]]

    if state[1:-3] == nstat:
        prev = sum([i + l for i, c in enumerate(state[4:]) if c == "#"])
        curr = sum([i + l + 1 for i, c in enumerate(nstat[3:]) if c == "#"])
        print(prev + (50000000000 - c) * (curr - prev)) 
        break

    state = nstat

    l -= 2
    while state[0] == ".":
        state = state[1:]
        l += 1
    state = state.strip(".")
