_, prog = open("input").read().split("\n\n")
prog = list(map(int, prog[8:].strip().split(",")))

def step(a):
    b = a % 8
    b = b ^ 1
    c = a // 2 ** b
    b = b ^ c
    b = b ^ 4
    return b % 8


best = 10 ** 20
def search(i=0, valid_suffix=None, n=0):
    global best
    if i == len(prog):
        if valid_suffix == 0:
            best = min(best, n)
        return

    for x in range(1024):
        if valid_suffix is not None and x & (2 ** 7 - 1) != valid_suffix:
            continue

        if step(x) == prog[i]:
            search(i + 1, x >> 3, ((x % 8) << (3 * i)) + n)


search()
print(best)
