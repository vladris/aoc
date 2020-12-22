input = open("input").readlines()

layers = {}
for line in input:
    i, j = tuple(map(int, line.split(":")))
    layers[i] = (j - 1) * 2

def check(t):
    for l in layers:
        if (t + l) % layers[l] == 0:
            return False
    return True

t = 0
while not check(t):
    t += 1

print(t)
