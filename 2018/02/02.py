input = open("input").readlines()

for line in input:
    for line2 in input:
        if line == line2:
            continue

        diff = 0
        for a, b in zip(line, line2):
            if a != b:
                diff += 1
            if diff > 1:
                break

        if diff == 1:
            for a, b in zip(line, line2):
                if a == b:
                    print(a, end="")
            exit()
