import re

input = open("input").read()

rules, ss = input.strip().split("\n\n")
rules, ss = rules.split("\n"), ss.split("\n")

r = {}

for rule in rules:
    i, rest = rule.split(":")
    if '"' in rest:
        r[int(i)] = rest.split('"')[1]
    else:
        r[int(i)] = [tuple(map(int, s.strip().split(" "))) for s in rest.split("|")]

def compile(rule):
    if isinstance(r[rule], str):
        return r[rule]

    if rule != 11:
        result = "(" + "|".join(["".join([compile(x) for x in item]) for item in r[rule]]) + ")"
    else:
        opts = []
        for i in range(1,10):
            opts.append("((" + compile(42) + "){" + str(i) + "}(" + compile(31) + "){" + str(i) + "})")
        result = "(" + "|".join(opts) + ")"

    if rule == 8:
        result += "+"

    return result 

x = "^" + compile(0) + "$"

print(sum([re.match(x, s) != None for s in ss]))
