from itertools import combinations

input = open("input").readlines()

total = 0
for line in input:
    nums = list(map(int, line.split("\t")))
    for a, b in combinations(nums, 2):
        a, b = max(a, b), min(a, b)
        if a % b == 0:
            total += a // b
            break

print(total)
