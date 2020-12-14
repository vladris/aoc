import re

mem = {}

for line in open("input").readlines():
    m = re.match(r"mask = (.{36})\n$", line)
    if m:
        ones, zeros = 0, 0
        for i, c in enumerate(m[1]):
            if c == "1":
                ones |= 1 << (35 - i)
            elif c == "0":
                zeros |= 1 << (35 - i)
        continue

    m = re.match(r"mem\[(\d+)\] = (\d+)", line)
    mem[m[1]] = (int(m[2]) | ones) & ~zeros

print(sum(mem.values()))
