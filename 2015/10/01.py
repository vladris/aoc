nums = "1113222113"

def step(nums):
    new, i = "", 0

    while i < len(nums):
        count = 1
        while i < len(nums) - 1 and nums[i] == nums[i + 1]:
            i += 1
            count += 1
        new += str(count) + nums[i]
        i += 1

    return new

for i in range(40):
    nums = step(nums)

print(len(nums))