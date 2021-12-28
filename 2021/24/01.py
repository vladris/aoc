program = open("input").readlines()

def run(inp):
    i, vars = 0, {c: 0 for c in "wxyz"}

    val = lambda c: vars[c] if c in vars else int(c)

    for line in program:
        match line.strip().split():
            case "inp", a:
                vars[a] = n[i]
                i += 1
            case "add", a, b:
                vars[a] += val(b)
            case "mul", a, b:
                vars[a] *= val(b)
            case "div", a, b:
                vars[a] //= val(b)
            case "mod", a, b:
                vars[a] %= val(b)
            case "eql", a, b:
                vars[a] = int(vars[a] == val(b))

    return vars["z"] == 0

# Determined by reverse engineering :)
n = [5, 1, 9, 3, 9, 3, 9, 7, 9, 8, 9, 9, 9, 9]

assert(run(n))

print("".join(map(str, n)))
