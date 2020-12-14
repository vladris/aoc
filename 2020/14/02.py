import re

mem = {}

def set(at, xs, value):
    if not xs:
        mem[at] = value
        return

    set(at | (1 << xs[0]), xs[1:], value)
    set(at & ~(1 << xs[0]), xs[1:], value)

for line in open("input").readlines():
    m = re.match(r"mask = (.{36})", line)
    if m:
        ones, xs = 0, []
        for i, c in enumerate(m[1]):
            if c == "1":
                ones |= 1 << (35 - i)
            elif c == "X":
                xs.append(35 - i)
        continue

    m = re.match(r"mem\[(\d+)\] = (\d+)", line)
    set(int(m[1]) | ones, xs, int(m[2]))

print(sum(mem.values()))
