input = open("input").readlines()

total = 0
for line in input:
    nums = list(map(int, line.split("\t")))
    total += max(nums) - min(nums)

print(total)
