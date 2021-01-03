input = open("input").readlines()

state = input[0][15:].strip()
rules = {}

for line in input[2:]:
    p, r = line.strip().split(" => ")
    rules[p] = r

l = 0

for _ in range(20):
    nstat = ""
    state = "...." + state + "...."
    for i in range(len(state) - 4):
        nstat += rules[state[i:i + 5]]
    state = nstat
    l -= 2

print(sum([i + l for i, c in enumerate(state) if c == "#"]))
