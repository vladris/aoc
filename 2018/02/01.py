input = open("input").readlines()

twos, threes = 0, 0
for line in input:
    counts = {}
    for c in line.strip():
        if c not in counts:
            counts[c] = 0
        counts[c] += 1

    for c in counts:
        if counts[c] == 2:
            twos += 1
            break
    
    for c in counts:
        if counts[c] == 3:
            threes += 1
            break

print(twos * threes)
