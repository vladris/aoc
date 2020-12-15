input = [12, 20, 0, 6, 1, 17, 7]

nums, last = {n: i for i, n in enumerate(input[:-1])}, input[-1]

for i in range(len(input) - 1, 2019):
    if last in nums:
        old = nums[last]
        nums[last] = i
        last = i - old
    else:
        nums[last] = i
        last = 0

print(last)
