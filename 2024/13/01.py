import re

machines = [re.findall(r"(\d+)", machine) for machine in open("input").read().split("\n\n")]
machines = [list(map(int, machine)) for machine in machines]

total = 0
for machine in machines:
    tokens = 10 ** 5
    for i in range(101):
        ax, ay = machine[0] * i, machine[1] * i
        for j in range(101):
            bx, by = machine[2] * j, machine[3] * j
            if ax + bx == machine[4] and ay + by == machine[5]:
                if i * 3 + j < tokens:
                    tokens = i * 3 + j
    if tokens != 10 ** 5:
        total += tokens

print(total)
