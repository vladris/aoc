lines = open("input").readlines()

def nice(line):
    if sum([s in line for s in ["ab", "cd", "pq", "xy"]]):
        return False

    if sum([c in "aeiou" for c in line]) < 3:
        return False

    if sum([cc[0] == cc[1] for cc in zip(line, " " + line)]) == 0:
        return False
    
    return True

print(sum([nice(line) for line in lines]))