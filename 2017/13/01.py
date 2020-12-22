input = open("input").readlines()

layers = {}
for line in input:
    i, j = tuple(map(int, line.split(":")))
    layers[i] = j

packet, state, cost = -1, { k: 0 for k in layers }, 0

while packet <= max(layers):
    packet += 1

    if packet in state and state[packet] == 0:
        cost += packet * layers[packet]

    for k in state:
        if state[k] == 0:
            state[k] = layers[k] * 2 - 3
        else:
            state[k] -= 1

print(cost)
