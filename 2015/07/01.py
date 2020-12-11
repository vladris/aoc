import re

lines = open("input").readlines()

wires = dict()

for line in lines:
    m = re.match(r"(\w+) (AND|OR|LSHIFT|RSHIFT) (\w+) -> (\w+)", line)
    if m:
        wires[m[4]] = m[2], m[1], m[3]
        continue

    m = re.match(r"NOT (\w+) -> (\w+)", line)
    if m:
        wires[m[2]] = "NOT", m[1], None
        continue

    m = re.match(r"(\w+) -> (\w+)", line)
    if m:
        wires[m[2]] = "SET", m[1], None

def get(at):
    if re.match(r"\d+", at):
        return int(at)

    if isinstance(wires[at], int):
        return wires[at]

    op, m1, m2 = wires[at]
    if   op == "SET"     : wires[at] = get(m1)
    elif op == "NOT"   : wires[at] = ~get(m1)
    elif op == "AND"   : wires[at] = get(m1) & get(m2)
    elif op == "OR"    : wires[at] = get(m1) | get(m2)
    elif op == "LSHIFT": wires[at] = get(m1) << get(m2)
    elif op == "RSHIFT": wires[at] = get(m1) >> get(m2)

    return wires[at]

print(get("a"))