input = open("input").read()

input = list(map(int, input.split(" ")))

def readnode(inp, i):
    children, metadata = inp[i], inp[i + 1]
    total = 0
    i += 2
    for _ in range(children):
        i, m = readnode(inp, i)
        total += m
    for _ in range(metadata):
        total += inp[i]
        i += 1
    return i, total

print(readnode(input, 0)[1])
