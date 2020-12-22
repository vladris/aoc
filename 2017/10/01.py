input = list(map(int, open("input").read().split(",")))

nums = list(range(256))

def reverse(f, t):
    while f != t:
        nums[f], nums[t] = nums[t], nums[f]
        f = (f + 1) % len(nums)
        if f == t:
            return
        t = (t - 1) % len(nums)

pos, skip = 0, 0
for l in input:
    if l != 0:
        reverse(pos, (pos + l - 1) % len(nums))
    pos = (pos + l + skip) % len(nums)
    skip += 1

print(nums[0] * nums[1])
