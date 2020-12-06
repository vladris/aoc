from functools import reduce

input = open("input").read().split("\n\n")

total = 0
for inp in input:
    total += len(reduce(set.union, map(set, inp.split("\n"))))

print(total)