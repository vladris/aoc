import re

input = open("input").read()

m = re.match(r".*(\w).\n.* (\d+) steps", input, flags=re.MULTILINE)
state = m[1]
steps = int(m[2])

rules = {}
for m in re.finditer(r"In state (\w).\n.*(\d):\n.*(\d)\.\n.*(left|right)\.\n.*(\w)\.\n.*(\d):\n.*(\d)\.\n.*(left|right)\.\n.*(\w)\.", input, flags=re.MULTILINE):
    rules[m[1]] = {
        int(m[2]): (int(m[3]), -1 if m[4] == "left" else 1, m[5]),
        int(m[6]): (int(m[7]), -1 if m[8] == "left" else 1, m[9])
    }

tape, head = {}, 0
for _ in range(steps):
    if head not in tape:
        tape[head] = 0
    
    rule = rules[state][tape[head]]
    tape[head] = rule[0]
    head += rule[1]
    state = rule[2]

print(sum(tape.values()))
