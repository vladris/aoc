input = open("input").readlines()

def eval(expr, i=0):
    vals, ops = [], []
    while expr[i] not in "\n)":
        while expr[i] == " ":
            i += 1

        if expr[i] == "(":
            i, v = eval(expr, i + 1)
            vals.append(v)
        elif expr[i] in "+*":
            ops.append(expr[i])
        elif expr[i].isdigit():
            vals.append(int(expr[i]))

        if len(vals) > len(ops) > 0 and ops[-1] == "+":
            ops.pop()
            vals.append(vals.pop() + vals.pop())

        i += 1

    while len(vals) > 1:
        vals.append(vals.pop() * vals.pop())

    return i, vals[0]

print(sum(map(lambda x: x[1], map(eval, input))))
