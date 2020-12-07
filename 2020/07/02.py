import re

lines = open("input").readlines()

rules = {}
for line in lines:
    bag = re.match(r"(\w+ \w+) bags contain", line)[1]
    rules[bag] = {}
    for rule in line[len(bag) + 13:].strip().split(","):
        m = re.match(r".*(\d+) (\w+ \w+)", rule)
        if not m:
            continue

        rules[bag][m[2]] = int(m[1])

def add(bag):
    total = 1
    if bag not in rules:
        return total

    for required in rules[bag]:
        total += rules[bag][required] * add(required)
    return total

print(add("shiny gold") - 1)