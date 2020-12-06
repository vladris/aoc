from functools import reduce

input = open("input").read().strip().split("\n\n")

total = 0
for inp in input:
    total += len(reduce(set.intersection, map(set, inp.split("\n"))))

print(total)