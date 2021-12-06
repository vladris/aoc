fish = map(int, open("input").readline().split(","))

clocks = {i: 0 for i in range(9)}

for f in fish:
    clocks[f] += 1

for _ in range(80):
    new = clocks[0]
    for i in range(8):
        clocks[i] = clocks[i + 1]
    clocks[8] = new
    clocks[6] += new

print(sum(clocks.values()))
