input = open("input").read()

input = list(map(int, input.split(" ")))

def readnode(inp, i):
    children, metadata = inp[i], inp[i + 1]
    i += 2

    if children == 0:
        total = 0
        for _ in range(metadata):
            total += inp[i]
            i += 1
        return i, total

    totals = {}
    for c in range(children):
        i, m = readnode(inp, i)
        totals[c + 1] = m

    total = 0
    for _ in range(metadata):
        if inp[i] in totals:
            total += totals[inp[i]]
        i += 1
    return i, total

print(readnode(input, 0)[1])
