rules, updates = open("input").read().split("\n\n")

rules = [(int(x), int(y)) for x, y in (rule.split("|") for rule in rules.split("\n"))]
updates = [[int(x) for x in update.split(",")] for update in updates.split("\n")]

def rules_for(x):
    return [rule[1] for rule in rules if rule[0] == x]


def make_valid(update):
    for i in range(len(update)):
        for y in rules_for(update[i]):
            if y in update[:i]:
                update[update[:i].index(y)], update[i] = update[i], update[update[:i].index(y)]
                return False, update
            
    return True, update


total = 0
for update in updates:
    valid, result = make_valid(update)
    if valid:
        continue

    while not valid:
        valid, result = make_valid(result)
    total += result[len(result) // 2]


print(total)
