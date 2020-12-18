input = open("input").readlines()

total = 0
for line in input:
    mode, tls = 0, False
    for i in range(len(line) - 4):
        if line[i] == "[":
            mode = 1
        elif line[i] == "]":
            mode = 0
        elif line[i] == line[i + 3] and line[i + 1] == line[i + 2] and line[i] != line[i + 1]:
            if mode == 1:
                tls = False
                break
            tls = True
    total += tls

print(total)
