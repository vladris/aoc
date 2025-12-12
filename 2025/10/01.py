import re

lines = [line for line in open("input").readlines()]

def parse(line):
    m = re.match(r"(\[.*\])\s(\(.*\)\s+?)(\{.*\})", line)
    goal, options = m.group(1), m.group(2).strip().split()
    
    d = 0
    for i, c in enumerate(goal[1:-1]):
        d |= (c == "#") << i

    switches = []
    for opt in options:
        s = 0
        for c in opt[1:-1].split(","):
            s |= 1 << int(c)
        switches.append(s)

    return d, switches


def solve(goal, state, tail, presses=0):
    global best

    if goal == state:
        best = min(best, presses)
        return

    if not tail:
        return

    h = tail[0]
    solve(goal, state ^ h, tail[1:], presses + 1)
    solve(goal, state, tail[1:], presses)


total = 0
for line in lines:
    d, switches = parse(line)
    best = 1000
    solve(d, 0, switches[:])
    total += best

print(total)
