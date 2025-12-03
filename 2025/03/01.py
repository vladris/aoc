inp = [list(line.strip()) for line in open("input").readlines()]

total = 0
for jolts in inp:
    best = 0
    for i in range(len(jolts) - 1):
        for j in range(i + 1, len(jolts)):
            best = max(int(jolts[i] + jolts[j]), best)
    total += best

print(total)