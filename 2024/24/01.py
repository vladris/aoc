vals, gates = open("input").read().split("\n\n")

calc = {line.split(": ")[0]: int(line.split(": ")[1]) for line in vals.split("\n")}

def get_val(v):
    if not isinstance(calc[v], int):
        match calc[v][1]:
            case "AND":
                calc[v] = get_val(calc[v][0]) & get_val(calc[v][2])
            case "OR":
                calc[v] = get_val(calc[v][0]) | get_val(calc[v][2])
            case "XOR": 
                calc[v] = get_val(calc[v][0]) ^ get_val(calc[v][2])
    return calc[v]


for gate in gates.split("\n"):
    expr, to = gate.split(" -> ")
    calc[to] = expr.split(" ")

total = 0
for z in sorted(filter(lambda val: val.startswith("z"), calc), reverse=True):
    total <<= 1
    total |= get_val(z)

print(total)
