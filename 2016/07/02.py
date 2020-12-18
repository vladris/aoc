input = open("input").readlines()

total = 0
for line in input:
    bab, i = [], 0
    while i < len(line) - 3:
        if line[i] == "[":
            while line[i] != "]":
                i += 1
            i += 1

        if line[i] == line[i + 2] and line[i] != line[i + 1] and line[i + 1] != "[":
            bab.append(line[i + 1] + line[i] + line[i + 1])
        i += 1
        
    i = line.index("[")
    while i < len(line) - 3:
        if line[i] == "]":
            while i < len(line) and line[i] != "[":
                i += 1
            if i == len(line):
                break
            i += 1

        if line[i:i + 3] in bab:
            total += 1
            break
        i += 1

print(total)
