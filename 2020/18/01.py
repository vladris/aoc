import operator

input = open("input").readlines()

ops = {
    "+": operator.add,
    "*": operator.mul
}

def eval(expr, i=0):
    vs, op = [], None
    while expr[i] not in "\n)":
        while expr[i] == " ":
            i += 1

        if expr[i] == "(":
            i, v = eval(expr, i + 1)
            vs.append(v)
        elif expr[i] in "+*":
            op = ops[expr[i]]
        elif expr[i].isdigit():
            vs.append(int(expr[i]))

        if len(vs) > 1:
            vs = [op(vs[0], vs[1])]

        i += 1

    return i, vs[0]

print(sum(map(lambda x: x[1], map(eval, input))))
