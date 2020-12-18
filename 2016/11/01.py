from itertools import combinations

input = [
    ["PoG", "TmG", "TmM", "PmG", "RuG", "RuM", "CoG", "CoM"],
    ["PoM", "PmM"],
    [],
    []
]

states = {}

def encode(elevator, floors):
    return "|".join([str(elevator)] + [",".join(sorted(map(lambda i: i[-1], floor))) for floor in floors])
    #return "|".join([str(elevator)] + [",".join(sorted(floor)) for floor in floors])

def valid(floors):
    for floor in floors:
        if not any(map(lambda i: i[-1] == "G", floor)):
            continue
        for m in filter(lambda i: i[-1] == "M", floor):
            if m[:-1] + "G" not in floor:
                return False
    return True

def update(floors, src, dest, items):
    new = [floor[:] for floor in floors]
    new[src] = list(set(new[src]) - set(items))
    new[dest] += items
    return new

best = 100
def move(elevator, floors, d=0):
    global best

    if not valid(floors) or d >= best:
        return

    state = encode(elevator, floors)
    if state in states and states[state] <= d:
        return
    states[state] = d

    if len(floors[3]) == 10:
        best = d
        return

    for i in range(1, 3):
        for items in combinations(floors[elevator], i):
            if elevator < 3:
                move(elevator + 1, update(floors, elevator, elevator + 1, items), d + 1)
            if elevator > 0 and i == 1:
                move(elevator - 1, update(floors, elevator, elevator - 1, items), d + 1)
    
move(0, input)
print(best)
