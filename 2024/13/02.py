import re

machines = [re.findall(r"(\d+)", machine) for machine in open("input").read().split("\n\n")]
machines = [list(map(int, machine)) for machine in machines]
machines = [machine[:4] + [machine[4] + 10000000000000, machine[5] + 10000000000000] for machine in machines]

def solve(machine):
    j = (machine[5] * machine[0] - machine[4] * machine[1]) / (machine[3] * machine[0] - machine[2] * machine[1])
    i = (machine[4] - machine[2] * j) / machine[0]

    if not i.is_integer() or not j.is_integer():
        return 0
    else:
        return int(i * 3 + j)

print(sum([solve(machine) for machine in machines]))
