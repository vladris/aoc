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

    return "(" + "|".join(["".join([compile(x) for x in item]) for item in r[rule]]) + ")"

x = "^" + compile(0) + "$"

print(sum([re.match(x, s) != None for s in ss]))
