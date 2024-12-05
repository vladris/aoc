rules, updates = open("input").read().split("\n\n")

rules = [(int(x), int(y)) for x, y in (rule.split("|") for rule in rules.split("\n"))]
updates = [[int(x) for x in update.split(",")] for update in updates.split("\n")]

def rules_for(x):
    return [rule[1] for rule in rules if rule[0] == x]


def valid(update):
    for i in range(len(update)):
        for y in rules_for(update[i]):
            if y in update[:i]:
                return False
            
    return True


print(sum([update[len(update) // 2] for update in updates if valid(update)]))
