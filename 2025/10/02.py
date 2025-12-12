import re
from scipy.optimize import milp, LinearConstraint, Bounds

lines = [line for line in open("input").readlines()]

def parse(line):
    m = re.match(r"(\[.*\])\s(\(.*\)\s+?)(\{.*\})", line)
    options, joltage = m.group(2).strip().split(), m.group(3)
    
    joltage = [int(x) for x in joltage[1:-1].split(",")]
    options = [list(map(int, opt[1:-1].split(","))) for opt in options]

    return options, joltage


def solve(options, joltage):
    n = len(options)
    matrix = [[options[j][i] for j in range(n)]
         for i in range(len(joltage))]

    res = milp(
        c=[1] * n,
        constraints=LinearConstraint(matrix, joltage, joltage),
        bounds=Bounds(lb=[0] * n, ub=[max(joltage)] * n),
        integrality=[1] * n,
    )

    return sum([int(round(x)) for x in res.x])


total = 0
for line in lines:
    options, joltage = parse(line)
    options = [[int(i in option) for i in range(len(joltage))] for option in options]

    total += solve(options, joltage)

print(total)
