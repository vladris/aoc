nums = list(map(int, open("input").readlines()))

for i in range(2, len(nums) - 1):
    for j in range(len(nums) - i + 1):
        r = nums[j:j + i]
        if sum(r) == 20874512:
            print(min(r) + max(r))
            exit()
