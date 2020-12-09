from itertools import combinations

nums = list(map(int, open("input").readlines()))

while any([c == nums[25] for c in map(sum, combinations(nums[:25], 2))]):
    nums = nums[1:]

print(nums[25])
