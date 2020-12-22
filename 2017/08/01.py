import re

input = open("input").readlines()

regs = {}

ops = {
    ">=": lambda x, y: x >= y,
    "<=": lambda x, y: x <= y,
    "<": lambda x, y: x < y,
    ">": lambda x, y: x > y,
    "==": lambda x, y: x == y,
    "!=": lambda x, y: x != y
}

for line in input:
    m = re.match(r"(\w+) (inc|dec) (-?\d+) if (\w+) (>=|<=|<|>|==|!=) (-?\d+)", line)

    if m[1] not in regs:
        regs[m[1]] = 0
    if m[4] not in regs:
        regs[m[4]] = 0

    if not ops[m[5]](regs[m[4]], int(m[6])):
        continue

    value = int(m[3])
    if m[2] == "dec":
        value *= -1
    regs[m[1]] += value
    
print(max(regs.values()))
