import re

lines = open("input").readlines()

rules = {}
for line in lines:
    bag = re.match(r"(\w+ \w+) bags contain", line)[1]
    for rule in line[len(bag) + 13:].strip().split(","):
        m = re.match(r".*(\d+) (\w+ \w+)", rule)
        if not m:
            continue

        if m[2] not in rules:
            rules[m[2]] = []
        rules[m[2]] += [bag]

bags = { "shiny gold" }
visited = set()

while bags:
    bag = bags.pop()
    if bag not in rules:
        visited.add(bag)

    if bag in visited:
        continue

    bags = bags.union(set(rules[bag]))
    visited.add(bag)

print(len(visited) - 1)