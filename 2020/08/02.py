lines = open("input").readlines()

instrs = []
for line in lines:
    instr, val = line.split()
    instrs.append((instr, int(val)))

def run(instrs):
    visited, acc, ip = set(), 0, 0
    while ip not in visited and ip != len(instrs):
        visited.add(ip)

        if instrs[ip][0] == "jmp":
            ip += instrs[ip][1]
            continue

        if instrs[ip][0] == "acc":
            acc += instrs[ip][1]
        ip += 1

    return None if ip != len(instrs) else acc

for i in range(len(instrs)):
    if instrs[i][0] == "acc":
        continue

    updated = "nop" if instr == "jmp" else "jmp"
    result = run(instrs[:i] + [(updated, instrs[i][1])] + instrs[i + 1:])
    if result != None:
        print(result)
        break
