gates = open("input").read().split("\n\n")[1]

calc = {f"x{i:02}": f"x{i:02}" for i in range(45)} | {f"y{i:02}": f"y{i:02}" for i in range(45)}
for gate in gates.split("\n"):
    expr, to = gate.split(" -> ")
    calc[to] = sorted(expr.split(" "))


def op_n(key, op, n):
    return calc[key] == [op, f"x{n:02}", f"y{n:02}"]


def find_key(value):
    for key in calc:
        if calc[key] == value:
            return key


def find_subtree(root_op, op, n):
    for key in calc:
        if calc[key][0] == root_op and (op_n(calc[key][1], op, n) or op_n(calc[key][2], op, n)):
            return key


def check_or(key, n):
    if n == 0:
        if not op_n(key, "AND", 0):
            return key, find_key(["AND", f"x00", f"y00"])
        return

    if calc[key][0] != "OR":
        return key, find_subtree("OR", "AND", n)

    if op_n(calc[key][1], "AND", n):
        return check_and(calc[key][2], n)
    elif op_n(calc[key][2], "AND", n):
        return check_and(calc[key][1], n)
    else:
        return key, find_key(["AND", f"x{n:02}", f"y{n:02}"])


def check_and(key, n):
    if calc[key][0] != "AND":
        return key, find_subtree("AND", "XOR", n)

    if op_n(calc[key][1], "XOR", n):
        return check_or(calc[key][2], n - 1)
    elif op_n(calc[key][2], "XOR", n):
        return check_or(calc[key][1], n - 1)
    else:
        return key, find_key(["XOR", f"x{n:02}", f"y{n:02}"])


def check_z(n):
    if n == 0:
        if calc["z00"] != ["XOR", "x00", "y00"]:
            return "z00", find_key(["XOR", "x00", "y00"])
        else:
            return
    if n == 45:
        return check_or(f"z45", n - 1)

    z = calc[f"z{n:02}"]
    if z[0] != "XOR":
        return f"z{n:02}", find_subtree("XOR", "XOR", n)

    if op_n(z[1], "XOR", n):
        return check_or(z[2], n - 1)
    elif op_n(z[2], "XOR", n):
        return check_or(z[1], n - 1)
    else:
        if check_or(z[1], n - 1) is None:
            return z[2], find_key(["XOR", f"x{n:02}", f"y{n:02}"])
        else:
            return z[1], find_key(["XOR", f"x{n:02}", f"y{n:02}"])
    

result = []
for i in range(46):
    if (check := check_z(i)) is not None:
        x, y = check
        result += [x, y]
        calc[x], calc[y] = calc[y], calc[x]

print(",".join(sorted(result)))
