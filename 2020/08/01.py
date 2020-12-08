lines = open("input").readlines()

instrs = []
for line in lines:
    instr, val = line.split()
    instrs.append((instr, int(val)))

visited, acc, ip = set(), 0, 0

while ip not in visited:
    visited.add(ip)

    if instrs[ip][0] == "jmp":
        ip += instrs[ip][1]
        continue

    if instrs[ip][0] == "acc":
        acc += instrs[ip][1]
    ip += 1

print(acc)