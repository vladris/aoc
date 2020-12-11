lines = open("input").readlines()

def nice(line):
    c1, c2 = False, False
    for i in range(len(line) - 3):
        if not c1 and line[i:i + 2] in line[i + 2:]:
            c1 = True
        if not c2 and line[i] == line[i + 2]:
            c2 = True

    return c1 and c2

print(sum([nice(line) for line in lines]))